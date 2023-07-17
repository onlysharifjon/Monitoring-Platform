from django.db import models


class EduLevel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ma'lumotlar"
        verbose_name_plural = "Ma'lumoti"


class Specialty(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mutaxassislik"
        verbose_name_plural = "Mutaxassisliklar"


class ScientificDegree(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ilmiy daraja"
        verbose_name_plural = "Ilmiy darajalar"


class ScientificTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ilmiy unvon"
        verbose_name_plural = "Ilmiy unvonlar"


class ForeignLangs(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Chet tili"
        verbose_name_plural = "Chet tillari"


class Teacher(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="F.I.SH")
    birth_date = models.DateField(verbose_name="Tug'ilgan sanasi")
    birth_place = models.CharField(max_length=255, verbose_name="Tug'ilgan joyi")
    education_level = models.ForeignKey(EduLevel, models.CASCADE, verbose_name="Ma'lumoti",
                                        related_name="level_teachers")
    graduated_institution = models.CharField(max_length=255, verbose_name="Tamomlagan OTM")
    specialty = models.ForeignKey(Specialty, models.CASCADE, related_name="spec_teachers",
                                  verbose_name="Mutaxassisligi")
    scientific_degree = models.ForeignKey(ScientificDegree, models.CASCADE, related_name="sc_degree_teachers",
                                          verbose_name="Ilmiy darajasi")
    scientific_title = models.ForeignKey(ScientificTitle, models.CASCADE, related_name="sc_title_teachers",
                                         verbose_name="Ilmiy unvoni")
    foreign_langs = models.ManyToManyField(ForeignLangs, "flang_teachers", verbose_name="Chet tillarini bilish",
                                           blank=True)
    work_starting_date = models.DateField(null=True, blank=True, verbose_name="Qachon ishga kirgan")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"


class Subject(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Room(models.Model):
    title = models.CharField(max_length=30, verbose_name="Xona")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"


class Group(models.Model):
    title = models.CharField(max_length=30, verbose_name="Guruh(yoki Patok)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Guruh(yoki Patok)"
        verbose_name_plural = "Guruh(yoki Patok)lar"


class Lesson(models.Model):
    lesson_types = (
        (1, "Ma'ruza"),
        (2, "Amaliy"),
        (3, "Boshqa")
    )
    wk_days = (
        (1, "Dushanba"),
        (2, "Seshanba"),
        (3, "Chorshanba"),
        (4, "Payshanba"),
        (5, "Juma"),
        (6, "Shanba"),
        (7, "Yakshanba"),
    )
    teacher = models.ForeignKey(Teacher, models.CASCADE, "teacher_lessons", "O'qituvchi")
    subject = models.ForeignKey(Subject, models.CASCADE, related_name="subject_lessons", verbose_name="Fan")
    lesson_type = models.IntegerField(choices=lesson_types, verbose_name="Dars turi", default=3)
    group = models.ForeignKey(Group, models.CASCADE, "group_lessons", verbose_name="Guruh(yoki Patok)")
    room = models.ForeignKey(Room, models.CASCADE, "room_lessons", verbose_name="Xona")
    time = models.TimeField(verbose_name="Boshlash vaqti")
    duration = models.IntegerField(default=80, verbose_name="Davomiyligi(minutda)")
    week_day = models.IntegerField(choices=wk_days, verbose_name="Hafta kuni")

    def __str__(self):
        return f"{self.subject.title} | {self.wk_days[self.week_day - 1][1]} | {self.time.strftime('%H:%M')}"

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"
