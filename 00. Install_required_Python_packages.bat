@echo off

TITLE [ Sprite_Atlas_Extractor ] 00_Install_required_Python_packages

echo.
echo.�ʼ� Python Package�� ��ġ�մϴ�.
echo.
echo.�� ������ ���� ó�� �� ���� �����ϸ� �˴ϴ�.
echo.(�Ʒ� Python Package�� �̼�ġ �Ǵ� ��ġ �� ���� �Ѵٸ� ���� �� Python Script�� ����� �� �����ϴ�.)
echo.
echo.[ Package List ]

type requirements.txt

echo.
echo.
echo.�� Package ��ġ�� �����Ϸ��� �ƹ� Ű�� �����ʽÿ� . . .
echo.

pause

python -m pip install -r requirements.txt

echo.
echo.�ʼ� Python Package ��ġ�� �Ϸ�Ǿ����ϴ�.
echo.
pause