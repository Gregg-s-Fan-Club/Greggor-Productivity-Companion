class TaskType(models.TextChoices):
    """ENUM for transaction types"""
    WORK: str = "work"
    SPORT: str = "sport"

class FilterTaskType(models.TextChoices):
    """ENUM for filter types"""
    ALL: str = "all"
    WORK: str = "work"
    SPORT: str = "sport"

    @staticmethod
    def get_list() -> list[str]:
        """Filter list for sent transactions"""
        return [FilterTransactionType.ALL]
