class ConfigSwitch:
    def __init__(self):
        # 每一小步调整间隔秒数
        self.interval_seconds = 10
        self.sleep_seconds = 1
        self.sub_count = 4

    @staticmethod
    def from_config(item):
        result = ConfigSwitch()
        result.interval_seconds = item["interval_seconds"]
        result.sleep_seconds = item["sleep_seconds"]
        result.sub_count = item["sub_count"]
        return result
