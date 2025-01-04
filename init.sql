-- Drop table if exists to ensure clean state
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS carrito;

-- Crear tabla de clientes con clave primaria y restricciones
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) UNIQUE NOT NULL,
  description VARCHAR(255) NOT NULL,
  price int not null
);

-- Crear tabla de usuarios
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

-- Crear tabla de correos confirmados
CREATE TABLE carrito (
  id INT REFERENCES users(id) ON DELETE SET NULL,
  product_id INT REFERENCES products(id) ON DELETE SET NULL,
  status VARCHAR(255) NOT NULL default 'pending',
  cant int not null
);

-- Insertar usuario admin solo si no existe
INSERT INTO users (email, password)
VALUES ('admin@localhost.com', '12345')
ON CONFLICT (email) DO NOTHING;