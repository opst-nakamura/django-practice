from django.shortcuts import render
from pathlib import Path
import os
 
def test(request):
    print("test動いてる")
    print(Path(__file__).resolve().parent.parent)
    print(Path(__file__).resolve().parent)
    print(Path(__file__).resolve())
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print("test動いてる")
    return render(request, "test.html")