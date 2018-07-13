#digunakan untuk nama elemen

class locator(object):

#registrasion elemen on register page https://sebangsa.com/register
    form_daftar          = "/html/body/div[1]/div/div[2]/div/div[2]/div"
    daf_akun             = "//*[@id='textId']"
    daf_email            = "//*[@id='textSurel']"
    daf_sandi1           = "//*[@id='textPwd']"
    daf_sandi2           = "//*[@id='textPwd2']"
    button_daftar2       = "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/p[2]/a"
    stiker               = "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/img"
    button_daftar_kanan  = "/html/body/div[1]/div/div[1]/div/div/nav/span/a[2]"
    button_masuk_kanan   = "/html/body/div[1]/div/div[1]/div/div/nav/span/a[1]"

#register on https://sebangsa.com/
    button_daftar1      = "/html/body/div[1]/div/div/div[1]/nav/div/div/a[2]/strong"
    form_register       = "/html/body/div[1]/div/div/div[1]/nav/div/div/div[2]/div/div/form/div[1]"
    f_akun              = "//*[@data-reactid='.0.1.0.0.0.1.3.0.0.0.0.1.2.0.1']"
    f_email             = "//*[@data-reactid='.0.1.0.0.0.1.3.0.0.0.0.2.0.0.1']"
    f_sandi1            = "//*[@data-reactid='.0.1.0.0.0.1.3.0.0.0.0.3.0.0.1']"
    f_sandi2            = "//*[@data-reactid='.0.1.0.0.0.1.3.0.0.0.0.4.0.0.1']"
    button_register     = "//*[@data-reactid='.0.1.0.0.0.1.3.0.0.0.0.6.0']"
    button_lewati       = "//*[@data-reactid='.0.1.0.1.0.0.0.0.0.0.1']"

#quickpass by register
    form_quickpass      = "//*[@data-reactid='.0.1.0.1.1']"
    q1                  = "//*[@data-reactid='.0.1.0.1.1.0.0.0.2.0.$1']"
    q2                  = "//*[@data-reactid='.0.1.0.1.1.0.0.0.2.0.$2']"
    q3                  = "//*[@data-reactid='.0.1.0.1.1.0.0.0.2.0.$4']"
    q4                  = "//*[@data-reactid='.0.1.0.1.1.0.0.0.2.0.$5']"
    q5                  = "//*[@data-reactid='.0.1.0.1.1.0.0.0.2.0.$6']"
    button_gabung       = "//*[@data-reactid='.0.1.0.1.1.0.0.0.5.1']"

#elemen sebangsa
    button_formlogin1    = "/html/body/div[1]/div/div/div[1]/nav/div/div/a[1]/strong"
    form_login           = "/html/body/div[1]/div/div/div[1]/nav/div/div/div[1]/div/div/form/div[1]"
    field_nama_akun      = "//*[@id='textId']"
    field_password       = "//*[@id='textPwd']"
    button_masuk         = "/html/body/div[1]/div/div/div[1]/nav/div/div/div[1]/div/div/form/div[1]/p[6]/button"

    avaprofil            = "/html/body/div[1]/div/div[1]/div/nav/div[5]/a"
    dropdown_ava         = "/html/body/div[1]/div/div[1]/div/nav/div[5]/div/ul"
    logout               = "/html/body/div[1]/div/div[1]/div/nav/div[5]/div/ul/li[4]/a"


    komunitas_tm         = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/a"
    senggolan_tm         = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/a"
    linimasa_tm          = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/a"
    panggung_tm          = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[4]/a"

    editor_posting       = "//*[@id='editorMainContainer']"
    button_posting       = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div[2]/span/input"
    body                 = "/html/body/div[1]/div/div[2]"

    detail_posting       = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/ul/li[5]/a"
    delete_posting       = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/ul/li[5]/div/ul/li[4]/a"

#elemen buat komunitas
    create_komunitas     = "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/section/div[2]/a"
    t_healt              = "//*[@data-reactid='.0.1.0.1.0.1.0.$0']"
    button_next          = "/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/a"
    f_nama_komunitas     = "//*[@id='group']"
    f_deskripsi          = "//*[@id='desc']"
    button_save          = "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[5]/div/a[2]"

#elemen buat komunitas
    btn_bt_senggolan     = "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/section/div[2]/a"
    btn_kll_senggolan    = "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/section/div[3]/a"
    form_senggolan       = "/html/body/div[1]/div/div[2]/div[2]"
    f_komunitas          = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/a"
    f_search_komunitas   = "//*[@id='Search']"
    kesehatan123         = "//*[@id='3351']"
    kategori_senggolan   = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/select"
    kategori_acara       = "//*[@data-reactid='.0.1.1.0.1.0.1.1.0.1.0.1:$0']"
    f_judul              = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/input"
    f_deskripsi          = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[4]/div[2]/textarea"
    gambar1              = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[5]/div[2]/div[1]/div[1]/input"
    gambar2              = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[5]/div[2]/div[1]/div[2]/input"
    gambar3              = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[5]/div[2]/div[1]/div[3]/input"
    gambar4              = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[5]/div[2]/div[1]/div[4]/input"
    btn_batal_senggol    = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div/div/div/a[1]"
    btn_simpan_senggol   = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div/div/div/a[2]"
    







    






