def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("请输入有效的整数！")

def format_currency(number):
    if number < 10000:
        return "¥ {} 元".format(int(number))
    return "¥ {:,.2f} 万".format(number / 10000)

def main():
    print("欢迎使用生活规划计算器！")
    
    # 获取用户输入
    expected_death_age = get_user_input("请输入预计死亡时年龄：")
    start_working_age = get_user_input("请输入预计开始工作时年龄：")
    retire_age = get_user_input("请输入预计躺平时年龄：")
    monthly_expenses = get_user_input("请输入躺平后计划的每月开销（单位：元）--例如7300元：")

    # 计算躺平时间和躺平后每年开销 和 工作时间
    retire_years = expected_death_age - retire_age
    annual_retire_expenses = 12 * monthly_expenses

    # 计算躺平所需总金额和平均工作每年时需要攒下的钱
    total_retire_expenses = annual_retire_expenses * retire_years
    working_years = retire_age - start_working_age
    avg_savings_per_year = total_retire_expenses / working_years

    # 固定金额
    fixed_medical_expenses = 1.2 * 10000  # 固定--每年医疗支出(不生大病就省钱，没生病节省的钱用来体检)
    fixed_social_insurance_expenses = 0.6 * 10000  # 固定-每年社保养老保险缴纳(30年)

    # 剩余金额
    remaining_expenses = annual_retire_expenses - fixed_medical_expenses - fixed_social_insurance_expenses

    # 按照比例分配剩余金额到其他花费项目
    ratios = [1.1, 1, 2, 1.2, 1.2, 1.2, 0.5, 0.6]
    total_ratio = sum(ratios)
    normalized_ratios = [r / total_ratio for r in ratios]
    other_expenses_distribution = [remaining_expenses * r for r in normalized_ratios]

    # 显示计算结果
    print("\n计算结果：")
    print(f"开始工作时年龄: {start_working_age} 岁")
    print(f"开始躺平时年龄: {retire_age} 岁")
    print(f"努力工作攒钱时间: {working_years} 年")
    print(f"躺平后每年开销: {format_currency(annual_retire_expenses)}")
    print(f"躺平所需总金额: {format_currency(total_retire_expenses)}")
    print(f"平均工作每年时需要攒下的钱: {format_currency(avg_savings_per_year)}")

    print("\n躺平后每年开销分配：")
    print(f"每月买菜自己做花费: {format_currency(other_expenses_distribution[0] / 12)}")
    print(f"每季度鞋服花费(旧衣服重复利用): {format_currency(other_expenses_distribution[1] / 4)}")
    print(f"每季度旅游花费: {format_currency(other_expenses_distribution[2] / 4)}")
    print(f"每月生活日用品花费: {format_currency(other_expenses_distribution[3] / 12)}")
    print(f"固定--每月医疗支出(不生大病就省钱，没生病节省的钱用来体检): {format_currency(fixed_medical_expenses / 12) }")
    print(f"每月交通出行(高铁、公交、打的、电瓶车、自行车、步行): {format_currency(other_expenses_distribution[4] / 12)}")
    print(f"每月节日礼品人际往来: {format_currency(other_expenses_distribution[5] / 12)}")
    print(f"每月外出聚餐: {format_currency(other_expenses_distribution[6] / 12)}")
    print(f"固定-每月社保养老保险缴纳(30年): {format_currency(fixed_social_insurance_expenses / 12 ) }")

if __name__ == "__main__":
    main()
