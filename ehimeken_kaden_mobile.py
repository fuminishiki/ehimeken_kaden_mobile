import folium

m = folium.Map(location=[33.5146152,132.9078149],zoom_start=9)
m

folium.Marker(location=[33.9532036,133.2696946],popup='エディオン イオンモール新居浜店　　　　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.0593606,132.9817729],popup='エディオン 今治本店　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[33.7913963,132.7165702],popup='エディオン エミフルMASAKI店　　　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[33.5280899,132.5655085],popup='エディオン 大洲店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[33.2364632,132.56818665],popup='エディオン 北宇和島店　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[33.4619627,132.420686],popup='エディオン フジグラン北浜店　　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[33.7952872,132.8348929],popup='エディオン フジグラン重信店　　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[33.8445392,132.7517108],popup='エディオン 松山本店　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[33.820946,132.7728827],popup='エディオン 南松山店　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.0503759,133.019055],popup='ヤマダデンキ テックランド今治店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.1774131,132.5518927],popup='ヤマダデンキ テックランド宇和島店　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.5322563,132.577979],popup='ヤマダデンキ テックランド大洲店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.9655826,133.3070104],popup='ヤマダデンキ テックランド新居浜店　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.3844384,132.5037678],popup='ヤマダデンキ テックランド西予店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.800763,132.7846606],popup='ヤマダデンキ テックランド松山本店　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.9179171,133.0756458],popup='ヤマダデンキ ヤマダアウトレット西条店　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.8644995,132.7498713],popup='ヤマダデンキ YAMADA web.com松山問屋町店　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.0376514,132.9950619],popup='ケーズデンキ 今治店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[33.2427412,132.5689067],popup='ケーズデンキ 宇和島店　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.0017485,133.5642275],popup='ケーズデンキ 四国中央店　　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[33.8648376,132.7514121],popup='ケーズデンキ 松山問屋町店　　　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[33.8305466,132.7573495],popup='ケーズデンキ 松山藤原店　　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[33.9551045,133.2675743],popup='イオンモバイル 新居浜店　　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[33.8238706,132.7766760],popup='イオンモバイル 松山店　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[33.8224911,132.7753894],popup='パソコン工房 松山店　　　　　　　　　',icon=folium.Icon(color="green")).add_to(m)
m

folium.Marker(location=[33.8369974,132.7651728],popup='マーキュリー 松山　　　　　　　　',icon=folium.Icon(color="white")).add_to(m)
m

m.save('ehimeken_kaden_mobile.html')
