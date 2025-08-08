// Jenkinsfile - 修复输入序列传递问题版

pipeline {
    agent any
    
    stages {
        stage('启动容器并挂载项目') {
            steps {
                script {
                    echo "创建并启动dixiacheng容器..."
                    bat '''
                        docker run -d ^
                            --name dixiacheng ^
                            -v %WORKSPACE%:/app ^
                            python:3.9-slim ^
                            tail -f /dev/null
                    '''
                    echo "容器启动成功，项目已挂载到/app目录"
                }
            }
        }
        
        stage('执行游戏脚本') {
            steps {
                script {
                    echo "进入容器并执行游戏..."
                    // 使用here-document语法确保输入序列正确传递
                    bat "docker exec dixiacheng sh -c \"cd /app && python game.py <<EOF
a
100
1
EOF\""
                }
            }
        }
    }
}
