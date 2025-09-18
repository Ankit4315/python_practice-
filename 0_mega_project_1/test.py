import pyttsx3
import time

# Method 1: Basic fix
print("Method 1: Basic approach")
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    
    print("Speaking...")
    engine.say("Can you hear this test?")
    engine.say("Can you hear this")
    engine.say("Can you")
    engine.runAndWait()
    
    # Force a pause
    time.sleep(2)
    print("Done with Method 1")
except Exception as e:
    print(f"Method 1 failed: {e}")

# Method 2: Using different driver
print("\nMethod 2: Using SAPI5 driver")
try:
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    
    print("Speaking...")
    engine.say("Testing SAPI5 driver")
    engine.runAndWait()
    
    time.sleep(2)
    print("Done with Method 2")
except Exception as e:
    print(f"Method 2 failed: {e}")

# Method 3: Manual event loop
print("\nMethod 3: Manual event loop")
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    
    print("Speaking...")
    engine.say("Testing manual event loop")
    
    # Start the event loop manually
    engine.startLoop(False)
    for i in range(50):  # Give it time to speak
        engine.iterate()
        time.sleep(0.1)
    engine.endLoop()
    
    print("Done with Method 3")
except Exception as e:
    print(f"Method 3 failed: {e}")

# Method 4: Force stop and restart
print("\nMethod 4: Force stop and restart")
try:
    engine = pyttsx3.init()
    engine.stop()  # Force stop any previous instance
    
    engine = pyttsx3.init('sapi5')  # Reinitialize
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    
    print("Speaking...")
    engine.say("Testing after force restart")
    engine.runAndWait()
    
    time.sleep(2)
    print("Done with Method 4")
except Exception as e:
    print(f"Method 4 failed: {e}")

print("\nIf none of these work, try installing pywin32:")
print("pip install pywin32")
print("Then restart your command prompt/terminal")