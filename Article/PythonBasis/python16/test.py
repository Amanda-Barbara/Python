import time

def add_component(func):
    def decorator_fun(*args, **kwargs):
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func(*args, **kwargs)

    return decorator_fun


@add_component
def punch(name, department):
    print('昵称：{0}  部门：{1} 上班打卡成功'.format(name, department))
# 相当于执行decorator_fun(name, department)

@add_component
def print_args(reason, **kwargs):
    print(reason)
    print(kwargs)
# 相当于执行decorator_fun(reason, **kwargs)

# punch('两点水', '做鸭事业部') # 相当于执行decorator_fun('两点水', '做鸭事业部')
add_component(punch('两点水', '做鸭事业部'))
# print_args('两点水', sex='男', age=99) # 相当于执行decorator_fun('两点水', sex = '男', age = 99)
