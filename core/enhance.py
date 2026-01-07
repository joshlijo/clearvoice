from df.enhance import enhance, init_df, load_audio, save_audio
from pathlib import Path

_model = None
_df_state = None


def load_model():
    global _model, _df_state
    if _model is None:
        _model, _df_state, _ = init_df()
    return _model, _df_state


def enhance_file(input_path: str, output_path: str):
    model, df_state = load_model()
    audio, _ = load_audio(input_path, sr=df_state.sr())
    enhanced = enhance(model, df_state, audio)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    save_audio(output_path, enhanced, df_state.sr())


if __name__ == "__main__":
    enhance_file(
        input_path="samples/noisy/noisy_1.wav",
        output_path="outputs/enhanced/noisy_1.wav",
    )