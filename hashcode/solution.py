no_of_contributors = int(input())
no_of_projects = int(input())
contributor = {}
for i in range(no_of_contributors):
    name, no_of_skill = input().split()
    skill_list = {}
    for j in range(int(no_of_skill)):
        skill_name, skill_level = input().split()
        skill_list[skill_name] = int(skill_level)
    contributor[name] = skill_list

projects = {}
for k in range(no_of_projects):
    name_project, days_completed, score, days_available, no_roles = input().split()
    days_available, days_completed = int(days_available), int(days_completed)
    roles = []
    for l in range(int(no_roles)):
        role_name, role_skil = input().split()
        roles.append([role_name,int(role_skil)])

