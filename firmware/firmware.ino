void setup()
{
    Serial.begin(115200);
}

void loop()
{
    while (Serial.available() > 0)
    {
        uint8_t val = Serial.read();
        if (val == '\n') 
        {
            Serial.println('r');
        }
    }
}
