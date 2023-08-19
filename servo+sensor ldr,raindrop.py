import RPi.GPIO as GPIO
import time

# Konfigurasi pin
servo_pin = 21
raindrop_pin = 17
ldr_pin = 18

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(raindrop_pin, GPIO.IN)
GPIO.setup(ldr_pin, GPIO.IN)

# Konfigurasi PWM untuk servo
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# Fungsi untuk mengatur sudut servo
def set_servo_angle(angle):
    duty_cycle = 2 + (angle/ 1)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5
               
                )

try:
    while True:
        # Baca nilai sensor raindrop
        raindrop_value = GPIO.input(raindrop_pin)

        # Baca nilai sensor LDR
        ldr_value = GPIO.input(ldr_pin)

        # Cek kondisi sensor raindrop
        if raindrop_value and ldr_value == GPIO.LOW:
            print("   TIDAK HUJAN")
            set_servo_angle(90) # Gerakkan servo ke sudut 90 derajat saat hujan terdeteksi
        else:
        
            print("   HUJAN") 
            set_servo_angle(0)   # Gerakkan servo ke sudut 0 derajat saat tidak ada hujan

        # Cek kondisi sensor LDR
        if ldr_value == GPIO.LOW:
            print("CERAH")
        else:
            print("GELAP/MENDUNG")

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()

