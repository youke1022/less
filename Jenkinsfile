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
                }
            }
        }
        
        stage('执行游戏脚本') {
            steps {
                script {
                    echo "通过逗号分隔参数执行游戏..."
                    // 新输入方式：直接传递 "a,100,1" 作为单次输入
                    bat '''
                        docker exec dixiacheng sh -c "cd /app && echo 'a,100,1' | python3 game.py"
                    '''  
                }
            }
        }
    }
}
