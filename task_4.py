# Исходные списки
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# 1. Перенос task_005 в completed_tasks
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# 2. Удаление task_007 из new_tasks
new_tasks.remove('task_007')

# 3. Вывод последней задачи из new_tasks (с повышенным приоритетом)
last_task = new_tasks[-1]
print(f"Следующая задача для работы: {last_task}")