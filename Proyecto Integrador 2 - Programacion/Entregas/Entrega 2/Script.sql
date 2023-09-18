CREATE DATABASE datos_sensor;

USE datos_sensor;

CREATE TABLE lectura_sensor (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Temperatura DECIMAL(5, 2),
    Humedad DECIMAL(5, 2),
    Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
