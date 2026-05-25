import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Aplikasi Data Siswa",
    page_icon="📚",
    layout="wide"
)

st.title(" Aplikasi Data Siswa")




username = st.sidebar.text_input("Masukkan Username")
password = st.sidebar.text_input("Masukkan Password", type="password")



if username == "admin" and password == "123":

    st.sidebar.success("Login berhasil")

    
    menu = st.sidebar.selectbox(
        "Pilih Menu",
        ["Dashboard", "Input Data", "Lihat Data"]
    )

    
    if menu == "Dashboard":
        st.header("Dashboard")
        st.info("Selamat datang di website data Siswa")


    
    elif menu == "Input Data":
        st.header("Input Data Siswa")

        nama = st.text_input("Masukkan Nama")
        umur = st.number_input("Masukkan Umur", 1, 100)
        kelas = st.selectbox(
            "Pilih Kelas",
            ["XI TKJ 1", "XI TKJ 2", "XI TKJ 3"]
        )

        if st.button("Simpan"):

            data_baru = pd.DataFrame({
                "Nama": [nama],
                "Umur": [umur],
                "Kelas": [kelas]
            })

            if os.path.exists("data.csv"):
                data_baru.to_csv(
                    "data.csv",
                    mode="a",
                    header=False,
                    index=False
                )
            else:
                data_baru.to_csv(
                    "data.csv",
                    index=False
                )

            st.success("Data berhasil disimpan")


    
    elif menu == "Lihat Data":
        st.header("data siswa")

        if os.path.exists("data.csv"):

            df = pd.read_csv("data.csv")

            
            keyword = st.text_input(
                "Cari Nama siswa"
            )

            if keyword:
                df = df[
                    df["Nama"].str.contains(
                        keyword,
                        case=False
                    )
                ]

            
            pilihan_kelas = st.selectbox(
                "Filter berdasarkan kelas",
                ["Semua"] + list(df["Kelas"].unique())
            )

            if pilihan_kelas != "Semua":
                df = df[
                    df["Kelas"] == pilihan_kelas
                ]

            # tampilkan data
            st.dataframe(df)

            # statistik sederhana
            st.write("Jumlah Data:", len(df))

            # tombol download
            st.download_button(
                "Download CSV",
                df.to_csv(index=False),
                "data_siswa.csv",
                "text/csv"
            )

        else:
            st.warning("Belum ada data")



else:
    st.sidebar.warning("Silakan login terlebih dahulu")