# AES - CTR Encryption
> AES CTR mode를 사용한 암호화, 복호화 프로그램입니다.

파이썬으로 작성되었기 때문에 파이썬 라이브러리를 받아야 합니다.  
기본적으로 `pip freeze`를 통해 라이브러리를 `requirements.txt`에 담아두었기 때문에 해당 파일을
이용하시길 바랍니다.

사용방법은 다음과 같습니다.


```bash
pip install -r requirements.txt
python main.py --enc <filename>
python main.py --dec <filename>
```

위와 같이 `--enc`를 입력한 후 파일이름을 적게 되면 암호화를 시작합니다.
암호화를 시작하게 되면 패스워드를 입력으로 받습니다. 패스워드를 입력하면 AES 암호화가 완료됩니다.

암호화가 끝나면 파일이름과 같은 이름을 가진 `.enc`, `.iv`파일이
만들어집니다. `.enc`파일은 암호화된 파일으로 AES-CTR 암호방식으로 암호화되었습니다.
`.iv`파일은 initial vector파일으로 암호화한 값을 복호화하기 위해 필요한 값 중 하나입니다.

복호화는 `.enc`파일을 타겟으로 잡고 `--dec`옵션을 주어 입력하면 됩니다.
처음 입력했던 key와 같은 암호를 적으면 다시 AES-CTR 암호방식으로 복호화 하여 기존의
값을 볼 수 있게 됩니다.