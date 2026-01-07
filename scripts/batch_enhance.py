from pathlib import Path
from core.enhance import enhance_file

input_dir = Path("samples/noisy")
output_dir = Path("outputs/enhanced")
output_dir.mkdir(parents=True, exist_ok=True)

for wav in sorted(input_dir.glob("*.wav")):
    out_path = output_dir / wav.name
    print(f"Enhancing {wav.name}")
    enhance_file(str(wav), str(out_path))