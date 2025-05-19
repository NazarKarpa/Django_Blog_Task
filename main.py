import django_setup
from Blog_app.models import Blog, Comment


# Створення записів у блозі
blog1 = Blog.objects.create(
    name="Як працює Django ORM",
    instead="У цій статті розглянемо, як Django працює з базами даних.",
    data_create="2025-05-01"
)

blog2 = Blog.objects.create(
    name="Основи Python",
    instead="Це вступна стаття для тих, хто починає працювати з Python.",
    data_create="2025-05-15"
)

# Створення коментарів
comment1 = Comment.objects.create(
    text="Дуже корисна стаття! Дякую!",
    author="Марія Іваненко",
    data="2025-05-02",
    comment_to=blog1
)

comment2 = Comment.objects.create(
    text="Хочу більше прикладів з кодом.",
    author="Олег Сидоренко",
    data="2025-05-03",
    comment_to=blog1
)

comment3 = Comment.objects.create(
    text="Чітке пояснення основ. Респект!",
    author="Анна Козак",
    data="2025-05-16",
    comment_to=blog2
)
