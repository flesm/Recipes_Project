from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Category, Recipes, Steps


def index(request):
    recipes = Recipes.objects.all()
    categories = Category.objects.all()
    context = {'categories': categories, 'recipes': recipes}

    return render(request, 'cooking_recipes/index.html', context)


def about(request):
    return render(request, 'cooking_recipes/about.html')


def login(request):
    return render(request, 'cooking_recipes/login.html')


def crt_rec(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'cooking_recipes/crt_rec.html', context)


def category_detail(request, ctg_slug):
    category = get_object_or_404(Category, slug=ctg_slug)
    recipes = Recipes.objects.filter(ctg=category)
    context = {'category': category, 'recipes': recipes}
    return render(request, 'cooking_recipes/category_detail.html',
                  context)  # дапісаць файл для атабражэння рэцэптаў, па выбранай катэгорыі


def create_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')
        ctg = request.POST.get('recipe_category')
        category = Category.objects.get(name=ctg)
        recipe = Recipes.objects.create(
            title=title,
            recipe_description=description,
            img=image,
            ctg=category,
            user_id=request.user.id
        )
        recipe.save()
        recipe_id = recipe.pk  # или recipe.id
        for key, value in request.POST.items():
            if key.startswith('step'):
                step_description = value
                step = Steps.objects.create(
                    step_description=step_description,
                    recipe_id=recipe_id,
                    user_id=request.user.id
                )
        return redirect('home')
    else:
        return render(request, 'cooking_recipes/crt_rec.html')

# def create_recipe(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.user = request.user
#             recipe.save()
#             recipe_id = recipe.pk
#             for key, value in request.POST.items():
#                 if key.startswith('step'):
#                     step_description = value
#                     step = Steps.objects.create(
#                         step_description=step_description,
#                         recipe_id=recipe_id,
#                         user_id=request.user.id
#                     )
#             return redirect('home')
#     else:
#         form = RecipeForm()
#     return render(request, 'cooking_recipes/crt_rec.html', {'form': form})


# def recipe(request, rec_slug):
#     recipe = get_object_or_404(Recipes, slug=rec_slug)
#     form = CommentForm()
#     context = {'recipe': recipe, 'form': form}
#     return render(request, 'cooking_recipes/recipe.html', context)

def recipe(request, rec_slug):
    recipe = get_object_or_404(Recipes, slug=rec_slug)
    # Если это POST-запрос, обрабатываем данные из формы
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # Проверяем валидность формы
        if form.is_valid():
            # Связываем комментарий с рецептом и пользователем
            comment = form.save(commit=False)
            comment.recipe_id = recipe
            comment.user_id = request.user
            # Сохраняем комментарий в базу данных
            comment.save()
            # Перенаправляем на ту же страницу
            return redirect('recipe', rec_slug=rec_slug)
    # Если это не POST-запрос, создаем пустую форму
    else:
        form = CommentForm()
    # Получаем список всех комментариев к рецепту
    comments = recipe.comments_set.all()
    # Передаем контекст в шаблон
    return render(request, 'cooking_recipes/recipe.html', {'recipe': recipe, 'form': form, 'comments': comments})

