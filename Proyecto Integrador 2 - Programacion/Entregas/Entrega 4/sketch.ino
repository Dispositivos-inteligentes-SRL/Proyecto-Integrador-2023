/*====================================================================
; "Sensor de temperatura con nivel de batería"
;
; Creado:   lunes 9 de octubre del 2023
; Procesador: ESP32
; Compilador:  Wokwi
; Autor: Ulises Ale
; Descripción: 
; El dispositivo esta diseñando para dar la información producida
; por el sensor DHT22, el nivel de Bateria a travez del led gráfico 
; y el accionar de un Actuador.
; Esquema eléctrico con los respectivos componentes al microcontrolador 
;
;====================================================================*/

#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

// Pin para el relé
const int relayPin = 12;

// Pin para el potenciómetro
const int potPin = 34;

// Pins para el LED bar graph
const int ledPins[] = {15, 2, 4, 5, 18, 19, 21, 22, 23, 13};

// Configuración del sensor DHT22
#define DHTPIN 14
#define DHTTYPE DHT22

DHT_Unified dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(relayPin, OUTPUT);
  dht.begin();
  Serial.begin(9600);

  // Configurar los pines del LED bar graph como salidas
  for (int i = 0; i < sizeof(ledPins) / sizeof(ledPins[0]); i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  float temperatura = event.temperature;
  dht.humidity().getEvent(&event);
  float humedad = event.relative_humidity;

  int valorPotenciometro = analogRead(potPin);
  int porcentajePotenciometro = map(valorPotenciometro, 0, 4095, 0, 100); // El ESP32 tiene un ADC de 12 bits

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print(" °C | Humedad: ");
  Serial.print(humedad);
  Serial.print(" % | Potenciómetro: ");
  Serial.print(porcentajePotenciometro);
  Serial.println(" %");

  if (porcentajePotenciometro >= 50) {
    digitalWrite(relayPin, HIGH);
  } else {
    digitalWrite(relayPin, LOW);
  }

  // Control del LED bar graph
  int ledsEncendidos = map(porcentajePotenciometro, 0, 100, 0, sizeof(ledPins) / sizeof(ledPins[0]));
  for (int i = 0; i < sizeof(ledPins) / sizeof(ledPins[0]); i++) {
    if (i < ledsEncendidos) {
      digitalWrite(ledPins[i], HIGH);
    } else {
      digitalWrite(ledPins[i], LOW);
    }
  }

  delay(1000);
}
