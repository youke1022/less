# @Version : 2.1
# @Time    : 2025/08/08
# @Author  : oeasy

import time
import sys


def parse_input(input_str):
    """解析逗号分隔的输入参数"""
    try:
        params = [item.strip() for item in input_str.split(',')]
        if len(params) != 3:
            raise ValueError("需要输入3个参数（职业,等级,怪物等级），例如：a,100,1")

        # 验证职业输入
        job = params[0].lower()
        if job not in ('a', 'b'):
            raise ValueError("职业必须是a或b")

        return job, int(params[1]), int(params[2])
    except ValueError as e:
        print(f"输入格式错误: {e}")
        sys.exit(1)


print('■■■■■■■■■■ 欢迎来到地下城，勇敢的少年 ■■■■■■■■■■')
print('''
     ,            _..._            ,
    {'.         .'     '.         .'}
    { ~ '.      _|=    __|_      .'  ~}
  { ~  ~ '-._ (___________) _.-'~  ~  }
 {~  ~  ~   ~.'           '. ~    ~    }
{  ~   ~  ~ /   /\     /\   \   ~    ~  }
{   ~   ~  /    __     __    \ ~   ~    }
 {   ~  /\/  -<( o)   ( o)>-  \/\ ~   ~}
  { ~   ;(      \/ .-. \/      );   ~ }
   { ~ ~\_  ()  ^ (   ) ^  ()  _/ ~  }
    '-._~ \   (`-._'-'_.-')   / ~_.-'
        '--\   `'._'+'_.'`   /--'
            \     \`-'/     /
             `\    '-'    /'
               `\       /'
                 '-...-' 
''')

# 直接要求逗号分隔输入
input_str = input("请输入参数（职业,等级,怪物等级），例如：a,100,1\n")
job, level, monsterLevel = parse_input(input_str)

# 角色属性计算
hp = att = defend = 0
if job == "a":
    hp = 800 + level * 59
    att = 100 + level * 10
    defend = 20 + level * 5
else:
    hp = 500 + level * 35
    att = 120 + level * 19
    defend = 15 + level * 3

print('你的等级是{}，攻击力{}，血量{}，防御力{}'.format(level, att, hp, defend))
print("■■■■■■■■■■■■■■■■■ 战斗开始 ■■■■■■■■■■■■■■■■■")

# 战斗逻辑
bosshp = 10000 + monsterLevel * 30
bossatt = 50 + monsterLevel * 8
bossdef = 50

while bosshp > 0 and hp > 0:
    hp -= max(0, bossatt - defend)
    print("怪物攻击了你，HP - {}，剩余HP：{}".format(max(0, bossatt - defend), hp))
    bosshp -= max(0, att - bossdef)
    print("你攻击了Boss，砍掉了 {} 点血，剩余HP：{}".format(max(0, att - bossdef), bosshp))
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    time.sleep(0.5)

if hp <= 0:
    print("战败，大侠请从头来过（试试把自己等级提高，怪物等级降低，再运行一次～）")
else:
    print("恭喜你战胜了Boss，爆到石中剑一把。")
    print('''
           ,
          / \\
         {   }
         !   !
         ; : ;
         | : |
         | : |
         l ; l
         l ; l
         I ; I
         I ; I
         I ; I
         I ; I
         d | b 
         H | H
         H | H
         H I H
 ,;,     H I H     ,;,
;H@H;    ;_H_;,   ;H@H;
`\Y/d_,;|4H@HK|;,_b\Y/'
 '\;MMMMM$@@@$MMMMM;/'
   ~~~*; !8@8!; *~~~
         ;888;
         ;888;
         ;888;
         ;888;
         d8@8b
         O8@8O
         T808T
          `~` 
''')
