# ─────────────────────────────────────────
# LOAD REFERENCE LABELS (optional)
# ─────────────────────────────────────────
REFERENCE_CSV   = "/kaggle/input/dl-sprint-4-0-bengali-long-form-speech-recognition/sample_submission .csv"
references = {}
if os.path.exists(REFERENCE_CSV):
    ref_df = pd.read_csv(REFERENCE_CSV)
    print("📋 CSV columns found:", ref_df.columns.tolist())
    print(ref_df.head(3))

    # Auto-detect filename column
    filename_col     = next((c for c in ref_df.columns if c.lower() in ["filename", "file", "id", "audio", "name"]), ref_df.columns[0])
    # Auto-detect transcription column
    transcription_col = next((c for c in ref_df.columns if c.lower() in ["transcription", "transcript", "text", "sentence", "label"]), ref_df.columns[1])

    print(f"\n✅ Using '{filename_col}' as filename, '{transcription_col}' as transcription")
    references = dict(zip(ref_df[filename_col], ref_df[transcription_col]))
    print(f"📋 Loaded {len(references)} reference transcriptions.\n")
