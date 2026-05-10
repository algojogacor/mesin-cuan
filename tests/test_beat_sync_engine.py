import pytest
from unittest.mock import MagicMock, patch
import sys
import os

# Mock dependencies before importing the engine
sys.modules['dotenv'] = MagicMock()
sys.modules['librosa'] = MagicMock()
sys.modules['soundfile'] = MagicMock()
sys.modules['requests'] = MagicMock()
sys.modules['google.genai'] = MagicMock()
sys.modules['google'] = MagicMock()
sys.modules['anthropic'] = MagicMock()
sys.modules['faster_whisper'] = MagicMock()
sys.modules['PIL'] = MagicMock()
sys.modules['googleapiclient'] = MagicMock()
sys.modules['google.auth'] = MagicMock()
sys.modules['tqdm'] = MagicMock()
sys.modules['APScheduler'] = MagicMock()
sys.modules['APScheduler.schedulers'] = MagicMock()
sys.modules['APScheduler.schedulers.background'] = MagicMock()

# Ensure root is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now we can safely import or patch
import engine.beat_sync_engine as beat_sync_engine

def test_get_audio_duration_success():
    """Test get_audio_duration returns correct duration when librosa is available."""
    with patch('engine.beat_sync_engine._require_librosa') as mock_require:
        mock_librosa = MagicMock()
        mock_require.return_value = mock_librosa

        # Mock y (audio data) and sr (sample rate)
        # Duration = len(y) / sr
        # Let's say sr = 22050, duration = 2.0s -> len(y) = 44100
        mock_y = [0] * 44100
        mock_sr = 22050
        mock_librosa.load.return_value = (mock_y, mock_sr)

        duration = beat_sync_engine.get_audio_duration("dummy.wav")

        assert duration == 2.0
        mock_librosa.load.assert_called_once_with("dummy.wav", sr=None, mono=True)

def test_get_audio_duration_librosa_missing():
    """Test get_audio_duration raises RuntimeError when librosa is not installed."""
    with patch('engine.beat_sync_engine._require_librosa') as mock_require:
        mock_require.side_effect = RuntimeError("librosa tidak terinstall!")

        with pytest.raises(RuntimeError) as excinfo:
            beat_sync_engine.get_audio_duration("missing_librosa.wav")

        assert "librosa tidak terinstall!" in str(excinfo.value)

def test_get_audio_duration_calculation():
    """Test the duration calculation logic itself."""
    with patch('engine.beat_sync_engine._require_librosa') as mock_require:
        mock_librosa = MagicMock()
        mock_require.return_value = mock_librosa

        # sr = 44100, len(y) = 66150 -> duration = 1.5s
        mock_y = [0] * 66150
        mock_sr = 44100
        mock_librosa.load.return_value = (mock_y, mock_sr)

        duration = beat_sync_engine.get_audio_duration("test.mp3")

        assert duration == 1.5
