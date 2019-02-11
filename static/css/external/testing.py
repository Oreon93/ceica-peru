SPANISHLEVEL = (
    ("b", "Beginner"),
    ("i", "Intermediate"),
    ("a", "Advanced"),
    ("d", "Different levels"),
)

GROUPNUMBER = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4 or more"),
)

current_spanish_level = models.CharField(default="b", max_length=1, choices=SPANISHLEVEL)
