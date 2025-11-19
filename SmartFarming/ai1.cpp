//Untuk sensor terhadap pertanian cerdas
#include <Arduino.h>

// Pin sensor LDR terhubung ke pin analog 34
const int LDR_PIN = 34;

void setup() {
Serial.begin(115200);  // Inisialisasi Serial Monitor
delay(1000);
Serial.println("ESP32 LDR Sensor Reading...");
}

void loop() {
// Membaca nilai analog dari LDR
int ldrValue = analogRead(LDR_PIN);

// Menampilkan nilai ke Serial Monitor
Serial.print("LDR Value: ");
Serial.println(ldrValue);

// Delay 500 ms sebelum membaca lagi
delay(500);
}
