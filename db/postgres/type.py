from dataclasses import dataclass


@dataclass
class DeviceType:
    EMETER: str = 'emeter'
    ZIGBEE: str = 'zigbee'
    LORA: str = 'lora'
    GSM: str = 'gsm'

    @classmethod
    def choice(cls):
        return (
            cls.EMETER, cls.ZIGBEE,
            cls.LORA, cls.GSM
        )
