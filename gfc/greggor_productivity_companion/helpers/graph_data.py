def category_bar_chart_data(user):
    tasks = user.get_user_tasks()

    periods = {7: [], 30: []}
    for period in periods.keys():
        categories = {}
        for task in tasks:
            workflows = task.get_task_workflows_over_period(period)
            for workflow in workflows:
                if task.category.name in categories.keys():
                    categories[task.category.name] += workflow.get_hours_spent() 
                else:
                    categories[task.category.name] = workflow.get_hours_spent() 
        data = []
        for key, value in categories.items():
            data.append([key, round(value, 2)])

        periods[period] = data
    return periods