#!/usr/bin/env python3
"""Start the preview once, whenever the Codespace starts or resumes."""
from pathlib import Path
from urllib.request import urlopen
import json
import os
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
PORT = int(os.environ.get('CHANGPO_PORT', '4173'))
RUNTIME = ROOT / '.preview'
RUNTIME.mkdir(exist_ok=True)

def ready():
    try:
        with urlopen(f'http://127.0.0.1:{PORT}/healthz', timeout=1) as response:
            return json.load(response).get('app') == 'changpo-private-preview'
    except Exception:
        return False

if not ready():
    with (RUNTIME / 'server.log').open('ab') as log:
        process = subprocess.Popen([sys.executable, str(ROOT / 'scripts' / 'serve.py')], cwd=ROOT,
                                   stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                                   start_new_session=True)
    (RUNTIME / 'server.pid').write_text(str(process.pid))
    for _ in range(40):
        if ready():
            break
        if process.poll() is not None:
            raise SystemExit('预览未能启动，请查看 .preview/server.log')
        time.sleep(.1)
    else:
        raise SystemExit('预览启动超时，请重新运行 python3 scripts/start_preview.py')

codespace = os.environ.get('CODESPACE_NAME')
if codespace and shutil.which('gh'):
    # No credentials are read or printed. GitHub supplies the Codespace identity.
    result = subprocess.run(['gh', 'codespace', 'ports', 'visibility', f'{PORT}:private',
                             '--codespace', codespace], capture_output=True, text=True)
    if result.returncode:
        print('请在 Ports 面板核对 4173 的 Visibility 为 Private。')
if codespace:
    domain = os.environ.get('GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN', 'app.github.dev')
    print(f'长坡私人预览已就绪：https://{codespace}-{PORT}.{domain}')
    print('请保留 Ports → Visibility → Private，仅你的 GitHub 登录身份可访问。')
else:
    print(f'长坡预览已就绪：http://127.0.0.1:{PORT}')
