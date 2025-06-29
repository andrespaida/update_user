# Update User Microservice

This microservice allows updating user information in the ToyShop platform. It uses JWT for authentication and connects to a PostgreSQL database.

## Technologies Used

- Python 3
- Flask
- psycopg2 (PostgreSQL driver)
- pyjwt (for token validation)
- flasgger (Swagger integration)
- Docker
- GitHub Actions

## Getting Started

### Prerequisites

- Python >= 3.8
- PostgreSQL
- pip

### Installation

```bash
git clone https://github.com/andrespaida/update_user.git
cd update_user
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory with the following content:

```env
PORT=3003
DB_HOST=your_postgres_host
DB_PORT=5432
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_NAME=your_postgres_database
JWT_SECRET=your_jwt_secret_key
```

### Running the Service

```bash
python app.py
```

The service will be running at `http://localhost:3003`.

### API Documentation (Swagger)

Once the service is running, Swagger UI will be available at:

```
http://localhost:3003/apidocs
```

Use it to explore and test the API endpoints.

## Available Endpoint

### PUT `/users/<int:user_id>`

Update an existing user's information. Requires a valid JWT token.

#### Headers:

```
Authorization: Bearer your.jwt.token
```

#### Request body (JSON):

```json
{
  "name": "Updated Name",
  "email": "updated@example.com",
  "password": "new_password",
  "role": "user"
}
```

#### Response (on success):

```json
{
  "message": "User updated successfully"
}
```

## Docker

To build and run the service using Docker:

```bash
docker build -t update-user .
docker run -p 3003:3003 --env-file .env update-user
```

## GitHub Actions Deployment

This project includes a GitHub Actions workflow for automatic deployment to an EC2 instance. Make sure to configure the following secrets in your GitHub repository:

- `EC2_HOST`
- `EC2_USERNAME`
- `EC2_KEY`
- `EC2_PORT` (optional, defaults to 22)

## License

This project is licensed under the MIT License.
