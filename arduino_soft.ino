#include "MPU9250.h"
#include <Wire.h>

MPU9250 mpu; // You can also use MPU9255 as is

void setup()
{
    Serial.begin(9600);
    Wire.begin();
    delay(2000);

    mpu.setup(0x68); // change to your own address

    delay(5000);

    // calibrate anytime you want to
    mpu.calibrateAccelGyro();
    mpu.calibrateMag();
}
void loop()
{
    if (mpu.update())
    {
        // Serial.print(mpu.getLinearAccX()); Serial.print(", ");
        // Serial.print(mpu.getLinearAccY()); Serial.print(", ");
        // Serial.print(mpu.getLinearAccZ()); Serial.print(", ");
        Serial.print(mpu.getYaw() + 180);
        Serial.print(", ");
        Serial.print(mpu.getPitch() + 180);
        Serial.print(", ");
        Serial.println(mpu.getRoll() + 180);
    }
}