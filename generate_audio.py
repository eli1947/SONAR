import numpy as np
from scipy.io.wavfile import write

def generate_float_4hz(filename, duration=60, sample_rate=44100):
    """Float: 4 Hz isochroon met pulserend adem-metronoom"""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Zachte 4 Hz brainwave stimulatie (sinusoïdale modulatie in plaats van harde pulsen)
    carrier_freq = 180  # Draaggolf frequentie
    # Zachte 4Hz modulatie voor brainwave entrainment zonder harde tikgeluiden
    isochronic_modulation = 0.5 * (1 + np.sin(2 * np.pi * 4 * t))
    
    # Genereer zachte 4Hz getone (effectieve sterkte voor brainwave entrainment)
    base_wave = 0.2 * np.sin(2 * np.pi * carrier_freq * t) * isochronic_modulation
    
    # Geïntegreerde ademmetronoom: 60 BPM amplitude modulatie van de draaggolf
    breath_freq = 60 / 60  # 60 BPM = 1 Hz
    # Gematigde ademgeleiding door amplitude variatie (30% modulatie - balans tussen beide effecten)
    breath_modulation = 1.0 + 0.3 * np.sin(2 * np.pi * breath_freq * t)
    
    # Pas ademmodulatie toe op de isochrone toon zelf
    base_wave_with_breath = base_wave * breath_modulation
    
    # Combineer (geen aparte metronoom meer nodig)
    combined_wave = base_wave_with_breath
    
    # Zacht fade-in aan het begin (eerste 5 seconden)
    fade_in_samples = int(5 * sample_rate)
    fade_in = np.linspace(0, 1, fade_in_samples)
    combined_wave[:fade_in_samples] *= fade_in
    
    # Stereo (zelfde signaal op beide kanalen)
    stereo_wave = np.column_stack((combined_wave, combined_wave))
    write(filename, sample_rate, (stereo_wave * 32767).astype(np.int16))

def generate_flow_12hz(filename, duration=60, sample_rate=44100):
    """Flow: 12 Hz binaural met golvende adem-metronoom"""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Echte binaural beats: 12 Hz verschil tussen oren
    base_freq = 220
    left_channel = 0.35 * np.sin(2 * np.pi * base_freq * t)
    right_channel = 0.35 * np.sin(2 * np.pi * (base_freq + 12) * t)
    
    # Geïntegreerde ademmetronoom: 100 BPM amplitude modulatie van de binaural beats
    breath_freq = 100 / 60  # 100 BPM = 1.67 Hz
    # Golvende ademgeleiding door amplitude variatie (15% modulatie voor subtiele flow)
    breath_modulation = 1.0 + 0.15 * np.sin(2 * np.pi * breath_freq * t)
    
    # Pas ademmodulatie toe op beide kanalen
    left_final = left_channel * breath_modulation
    right_final = right_channel * breath_modulation
    
    # Zacht fade-in aan het begin (eerste 5 seconden)
    fade_in_samples = int(5 * sample_rate)
    fade_in = np.linspace(0, 1, fade_in_samples)
    left_final[:fade_in_samples] *= fade_in
    right_final[:fade_in_samples] *= fade_in
    
    stereo_wave = np.column_stack((left_final, right_final))
    write(filename, sample_rate, (stereo_wave * 32767).astype(np.int16))

def generate_focus_50hz(filename, duration=60, sample_rate=44100):
    """Focus: 50 Hz zuivere binaural beats zonder metronoom"""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Zuivere binaural beats: 50 Hz verschil tussen oren
    # Lagere base frequency voor comfortabeler luisteren
    base_freq = 200  
    left_channel = 0.4 * np.sin(2 * np.pi * base_freq * t)
    right_channel = 0.4 * np.sin(2 * np.pi * (base_freq + 50) * t)
    
    # Zacht fade-in aan het begin (eerste 8 seconden voor focus opbouw)
    fade_in_samples = int(8 * sample_rate)
    fade_in = np.linspace(0, 1, fade_in_samples)
    left_channel[:fade_in_samples] *= fade_in
    right_channel[:fade_in_samples] *= fade_in
    
    # Zachte fade-out aan het einde (laatste 5 seconden)
    fade_out_samples = int(5 * sample_rate)
    fade_out = np.linspace(1, 0, fade_out_samples)
    left_channel[-fade_out_samples:] *= fade_out
    right_channel[-fade_out_samples:] *= fade_out
    
    # Geen metronoom - alleen zuivere binaural beats voor focus
    stereo_wave = np.column_stack((left_channel, right_channel))
    write(filename, sample_rate, (stereo_wave * 32767).astype(np.int16))

# Genereer de audiobestanden volgens specificaties
print("Genereren van SONAR audiobestanden...")
generate_float_4hz("float_4hz.wav")
print("✓ float_4hz.wav: 4 Hz isochroon met pulserend adem-metronoom")

generate_flow_12hz("flow_12hz.wav") 
print("✓ flow_12hz.wav: 12 Hz binaural met golvende adem-metronoom")

generate_focus_50hz("focus_50hz.wav")
print("✓ focus_50hz.wav: 50 Hz zuivere binaural zonder metronoom")

print("\nAlle audiobestanden succesvol gegenereerd!") 