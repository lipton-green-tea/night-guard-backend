import random
from datetime import datetime, timedelta
import numpy as np

def generate_random_bpm(start, end, num_samples,var):
    date_range = end - start
    date_list = [start + timedelta(days=x) for x in range(0, date_range.days + 1)]
    #generate random bpm with normal dist
    samples = [{"bpm": np.random.normal(65, var), "timestamp": (start + timedelta(seconds=random.randint(0, date_range.total_seconds()))).isoformat()} for i in range(num_samples)]
    return samples

def update_hr_summary(samples):
    bpms = [sample["bpm"] for sample in samples]
    avg_bpm = sum(bpms) / len(bpms)
    min_bpm = min(bpms)
    max_bpm = max(bpms)
    return {"avg_hr_bpm": avg_bpm, "min_hr_bpm": min_bpm, "max_hr_bpm": max_bpm}

def getbpm(num_samples, hrvar):
    start = datetime.now()
    end = start + timedelta(minutes=10)

    hr_samples = generate_random_bpm(start, end, num_samples,hrvar)
    hr_summary = update_hr_summary(hr_samples)

    data = {
    "data": [
        {
        "heart_rate_data": {
            "detailed": {
            "hrv_samples_sdnn": [],
            "hr_samples": hr_samples,
            "hrv_samples_rmssd": []
            },
            "summary": {
            "avg_hrv_rmssd": None,
            "hr_zone_data": [],
            "resting_hr_bpm": None,
            "user_max_hr_bpm": None,
            "avg_hr_bpm": hr_summary["avg_hr_bpm"],
            "avg_hrv_sdnn": None,
            "min_hr_bpm": hr_summary["min_hr_bpm"],
            "max_hr_bpm": hr_summary["max_hr_bpm"]
            }
        },
        "metadata": {
            "end_time": end.isoformat(),
            "start_time": start.isoformat(),
            "upload_type": 0
        },
        "device_data": {
            "activation_timestamp": None,
            "other_devices": [],
            "software_version": None,
            "serial_number": None,
            "name": None,
            "manufacturer": None,
            "hardware_version": None
        }
        }
    ],
    "user": {
        "last_webhook_update": None,
        "reference_id": None,
        "user_id": "fcb0b0a9-9a3c-4a5a-8fe1-c8aaf972fd76",
        "scopes": None,
        "provider": "GOOGLE"
    },
    "type": "daily"
    }
    return(data)