#!/usr/bin/env bash

pidFile="var/pids/supervisord.pid"
sockFile="var/run/supervisor.sock"

# 删除 sock 文件
echo "Begin delete sock file"
if [[ ! -e "${sockFile}" ]]; then
    echo "sock file has already deleted."
else
    rm ${sockFile}
fi

echo "Begin stop supervisor..."
if [[ ! -f "${pidFile}" ]]; then
    echo "Not have pid file."
    echo "Maybe supervisor has been stopped."
    exit 0
fi

# 获取进程 ID
sPid=$(cat ${pidFile})

# 获取平台
platform=$(uname)
echo "Now platform is ${platform}!"

# 检测进程是否存在
if [[ ${platform} == "Darwin" ]]; then
    if [[ "$(lsof -p "${sPid}")" ]]; then
        echo "Begin kill process for ${sPid}"
        KILL -9 "${sPid}"
    else
        echo "Process has already stopped."
    fi
else
    if [[ -d /proc/${sPid} ]]; then
        echo "Begin kill process for ${sPid}"
        KILL -9 "${sPid}"
    else
        echo "Process has already stopped."
    fi
fi

# 删除 pid 文件
echo "Begin delete pid file"
unlink ${pidFile}

echo "Supervisor stop finished."
