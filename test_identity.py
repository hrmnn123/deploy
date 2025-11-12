def test_page_contains_identity():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Sesuaikan teks di bawah ini dengan isi HTML kamu
    assert "<h1>Profil Hermansyah</h1>" in html, "Judul tidak ditemukan"
    assert "230411100020" in html, "NIM tidak ditemukan"
    assert "Hermansyah" in html, "Nama tidak ditemukan"
