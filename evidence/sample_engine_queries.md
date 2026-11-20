# Sample engine queries

Ini adalah respons aktual dari mesin analitik lokal yang sedang berjalan. Kelima pertanyaan ini mencakup seluruh lima tabel Gold. Mode mock memilih SQL yang sudah ditentukan sebelumnya untuk pertanyaan tolak ukur (benchmark) yang disediakan; hasil basis data dieksekusi terhadap basis data yang dikonfigurasi.

Baris maksimum yang diminta per pertanyaan: 1000. Seluruh baris yang dikembalikan disertakan di bawah ini. Angka harian menggunakan aturan tanggal UTC dari pipeline. Angka moneter mempertahankan unit asli dataset; tidak ada konversi mata uang yang diterapkan.

## 1. Berapa total pendapatan bersih berdasarkan saluran penjualan?

Analysis ID: analysis-b0f26c3d-ffcd-414a-bd5c-936e7f96b3c6
Tabel yang digunakan: gold.order_360
Baris dikembalikan: 4
Waktu eksekusi (ms): 39

### Jawabannya

Pendapatan bersih diagregasikan pada tingkat order (order grain) berdasarkan saluran penjualan. Mengembalikan 4 baris.

### SQL yang Dieksekusi

```sql
SELECT sales_channel, SUM(net_revenue) AS net_revenue FROM gold.order_360 GROUP BY sales_channel ORDER BY net_revenue DESC
```

### Data yang dikembalikan

| sales_channel | net_revenue |
| --- | --- |
| WEB | 3440808.22 |
| STORE | 3353874.46 |
| MOBILE_APP | 3340813.39 |
| MARKETPLACE | 3294328.76 |

### Definisi matrik mesin

- Pendapatan bersih diagregasikan pada tingkat order berdasarkan saluran penjualan.

### Peringatan dari mesin

Tidak ada yang dikembalikan oleh API untuk kueri ini.

### Visualisasi yang dikembalikan oleh mesin

```json
{
  "kind": "bar",
  "title": "What is total net revenue by sales channel? — comparison",
  "x": "sales_channel",
  "y": [
    "net_revenue"
  ],
  "color": null
}
```

## 2. Berapa banyak pelanggan yang aktif setiap hari?

ID Analisis: analysis-8f1fe704-471d-4dbb-a90e-7390b350d532
Tabel yang digunakan: gold.customer_daily
Baris dikembalikan: 90
Waktu eksekusi (ms): 48

### Jawabannya

Pelanggan aktif adalah pelanggan dengan setidaknya satu pesanan pada tanggal tersebut. Mengembalikan 90 baris.

### SQL yang dieksekusi

```sql
SELECT metric_date, COUNT(DISTINCT customer_id) AS active_customers FROM gold.customer_daily WHERE order_count > 0 GROUP BY metric_date ORDER BY metric_date
```

### Data yang dikembalikan

| metric_date | active_customers |
| --- | --- |
| 2026-06-22 | 121 |
| 2026-06-23 | 101 |
| 2026-06-24 | 108 |
| 2026-06-25 | 94 |
| 2026-06-26 | 104 |
| 2026-06-27 | 99 |
| 2026-06-28 | 107 |
| 2026-06-29 | 106 |
| 2026-06-30 | 100 |
| 2026-07-01 | 103 |
| 2026-07-02 | 113 |
| 2026-07-03 | 114 |
| 2026-07-04 | 114 |
| 2026-07-05 | 118 |
| 2026-07-06 | 100 |
| 2026-07-07 | 105 |
| 2026-07-08 | 121 |
| 2026-07-09 | 111 |
| 2026-07-10 | 117 |
| 2026-07-11 | 105 |
| 2026-07-12 | 115 |
| 2026-07-13 | 100 |
| 2026-07-14 | 84 |
| 2026-07-15 | 115 |
| 2026-07-16 | 124 |
| 2026-07-17 | 117 |
| 2026-07-18 | 131 |
| 2026-07-19 | 106 |
| 2026-07-20 | 114 |
| 2026-07-21 | 110 |
| 2026-07-22 | 108 |
| 2026-07-23 | 131 |
| 2026-07-24 | 98 |
| 2026-07-25 | 103 |
| 2026-07-26 | 122 |
| 2026-07-27 | 122 |
| 2026-07-28 | 115 |
| 2026-07-29 | 101 |
| 2026-07-30 | 103 |
| 2026-07-31 | 115 |
| 2026-08-01 | 91 |
| 2026-08-02 | 109 |
| 2026-08-03 | 114 |
| 2026-08-04 | 117 |
| 2026-08-05 | 121 |
| 2026-08-06 | 102 |
| 2026-08-07 | 94 |
| 2026-08-08 | 117 |
| 2026-08-09 | 102 |
| 2026-08-10 | 112 |
| 2026-08-11 | 101 |
| 2026-08-12 | 101 |
| 2026-08-13 | 92 |
| 2026-08-14 | 96 |
| 2026-08-15 | 94 |
| 2026-08-16 | 96 |
| 2026-08-17 | 90 |
| 2026-08-18 | 108 |
| 2026-08-19 | 112 |
| 2026-08-20 | 122 |
| 2026-08-21 | 112 |
| 2026-08-22 | 100 |
| 2026-08-23 | 108 |
| 2026-08-24 | 119 |
| 2026-08-25 | 112 |
| 2026-08-26 | 107 |
| 2026-08-27 | 126 |
| 2026-08-28 | 117 |
| 2026-08-29 | 98 |
| 2026-08-30 | 102 |
| 2026-08-31 | 118 |
| 2026-09-01 | 101 |
| 2026-09-02 | 113 |
| 2026-09-03 | 118 |
| 2026-09-04 | 126 |
| 2026-09-05 | 100 |
| 2026-09-06 | 97 |
| 2026-09-07 | 119 |
| 2026-09-08 | 112 |
| 2026-09-09 | 90 |
| 2026-09-10 | 107 |
| 2026-09-11 | 130 |
| 2026-09-12 | 114 |
| 2026-09-13 | 111 |
| 2026-09-14 | 116 |
| 2026-09-15 | 130 |
| 2026-09-16 | 99 |
| 2026-09-17 | 94 |
| 2026-09-18 | 102 |
| 2026-09-19 | 100 |

### Definisi metrik dari mesin

- Pelanggan aktif adalah pelanggan dengan setidaknya satu pesanan pada tanggal tersebut.

### Peringatan dari mesin

Tidak ada yang dikembalikan oleh API untuk kueri ini.

### Visualisasi yang dikembalikan oleh mesin

```json
{
  "kind": "line",
  "title": "How many customers were active each day? — trend",
  "x": "metric_date",
  "y": [
    "active_customers"
  ],
  "color": null
}
```

## 3. Apa saja produk teratas berdasarkan unit yang terjual?

Analysis ID: analysis-291b4046-5846-41a9-805b-597ba675d5da
Tabel yang digunakan: gold.product_daily
Baris dikembalikan: 80
Waktu eksekusi (ms): 37

### Jawabannya

Unit produk dijumlahkan dari fakta produk-harian (product-day facts). Mengembalikan 80 baris.

### SQL yang dieksekusi

```sql
SELECT product_id, SUM(units_sold) AS units_sold FROM gold.product_daily GROUP BY product_id ORDER BY units_sold DESC
```

### Data yang dikembalikan

| product_id | units_sold |
| --- | --- |
| PROD-00056 | 906 |
| PROD-00014 | 905 |
| PROD-00024 | 877 |
| PROD-00008 | 865 |
| PROD-00001 | 860 |
| PROD-00026 | 852 |
| PROD-00021 | 833 |
| PROD-00040 | 832 |
| PROD-00022 | 828 |
| PROD-00020 | 826 |
| PROD-00051 | 825 |
| PROD-00072 | 825 |
| PROD-00046 | 824 |
| PROD-00025 | 823 |
| PROD-00047 | 821 |
| PROD-00038 | 820 |
| PROD-00073 | 814 |
| PROD-00039 | 812 |
| PROD-00002 | 810 |
| PROD-00005 | 809 |
| PROD-00057 | 809 |
| PROD-00080 | 809 |
| PROD-00011 | 809 |
| PROD-00010 | 807 |
| PROD-00032 | 807 |
| PROD-00028 | 807 |
| PROD-00053 | 806 |
| PROD-00079 | 802 |
| PROD-00034 | 800 |
| PROD-00016 | 795 |
| PROD-00064 | 792 |
| PROD-00030 | 792 |
| PROD-00018 | 791 |
| PROD-00006 | 790 |
| PROD-00043 | 787 |
| PROD-00033 | 786 |
| PROD-00061 | 783 |
| PROD-00063 | 781 |
| PROD-00069 | 781 |
| PROD-00048 | 779 |
| PROD-00019 | 779 |
| PROD-00044 | 777 |
| PROD-00003 | 777 |
| PROD-00077 | 776 |
| PROD-00045 | 775 |
| PROD-00004 | 775 |
| PROD-00075 | 774 |
| PROD-00058 | 774 |
| PROD-00078 | 764 |
| PROD-00042 | 764 |
| PROD-00062 | 763 |
| PROD-00065 | 763 |
| PROD-00050 | 762 |
| PROD-00009 | 759 |
| PROD-00013 | 756 |
| PROD-00027 | 756 |
| PROD-00023 | 756 |
| PROD-00071 | 755 |
| PROD-00036 | 754 |
| PROD-00060 | 753 |
| PROD-00017 | 753 |
| PROD-00035 | 752 |
| PROD-00049 | 750 |
| PROD-00067 | 750 |
| PROD-00059 | 735 |
| PROD-00031 | 734 |
| PROD-00068 | 733 |
| PROD-00055 | 733 |
| PROD-00052 | 730 |
| PROD-00070 | 727 |
| PROD-00007 | 717 |
| PROD-00054 | 716 |
| PROD-00041 | 715 |
| PROD-00037 | 709 |
| PROD-00012 | 707 |
| PROD-00029 | 696 |
| PROD-00074 | 692 |
| PROD-00076 | 688 |
| PROD-00066 | 681 |
| PROD-00015 | 669 |

### Definisi metrik dari mesin

- Unit produk dijumlahkan dari fakta produk-harian.

### Peringatan dari mesin

Tidak ada yang dikembalikan oleh API untuk kueri ini.

### Visualisasi yang dikembalikan oleh mesin

```json
{
  "kind": "bar",
  "title": "What are the top products by units sold? — comparison",
  "x": "product_id",
  "y": [
    "units_sold"
  ],
  "color": null
}
```

## 4. Kampanye mana yang memiliki ROAS terbaik?

Analysis ID: analysis-ea7c39f6-b6ca-408e-a5bb-5529a3f6a860
Tabel yang digunakan: gold.channel_campaign_daily
Baris dikembalikan: 10
Waktu eksekusi (ms): 38

### Jawabannya

ROAS (Return on Ad Spend) adalah pendapatan bersih teratribusi dibagi dengan pengeluaran kampanye; kampanye tanpa pengeluaran dikecualikan dari pemeringkatan. Mengembalikan 10 baris.

### SQL yang dieksekusi

```sql
SELECT campaign_id, SUM(net_revenue) / NULLIF(SUM(campaign_spend), 0) AS roas FROM gold.channel_campaign_daily GROUP BY campaign_id HAVING SUM(campaign_spend) > 0 ORDER BY roas DESC
```

### Data yang dikembalikan

| campaign_id | roas |
| --- | --- |
| CMP-04 | 46.53800578280695 |
| CMP-05 | 45.88669339742113 |
| CMP-02 | 45.374094106393294 |
| CMP-09 | 45.3597590527384 |
| CMP-01 | 45.249023168540965 |
| CMP-06 | 44.42892679250748 |
| CMP-08 | 42.64380987023062 |
| CMP-07 | 41.577343672605636 |
| CMP-03 | 40.007846216136784 |
| CMP-10 | 39.27187768660647 |

### Definisi metrik dari mesin

- ROAS adalah pendapatan bersih teratribusi dibagi dengan pengeluaran kampanye; kampanye tanpa pengeluaran dikecualikan dari pemeringkatan.

### Peringatan dari mesin

Tidak ada yang dikembalikan oleh API untuk kueri ini.

### Visualisasi yang dikembalikan oleh mesin

```json
{
  "kind": "bar",
  "title": "Which campaigns had the best roas? — comparison",
  "x": "campaign_id",
  "y": [
    "roas"
  ],
  "color": null
}
```

## 5. Berapa pendapatan bersih harian?

Analysis ID: analysis-51449643-460a-426e-b345-25333e1496cb
Tabel yang digunakan: gold.executive_kpis_daily
Baris dikembalikan: 103
Waktu eksekusi (ms): 37

### Jawabannya

Tabel KPI eksekutif menyediakan metrik pendapatan bersih harian. Mengembalikan 103 baris.

### SQL yang dieksekusi

```sql
SELECT metric_date, net_revenue FROM gold.executive_kpis_daily ORDER BY metric_date
```

### Data yang dikembalikan

| metric_date | net_revenue |
| --- | --- |
| 2026-06-21 | 0.0 |
| 2026-06-22 | 148586.4 |
| 2026-06-23 | 150208.63 |
| 2026-06-24 | 128670.56 |
| 2026-06-25 | 121962.98 |
| 2026-06-26 | 139799.4 |
| 2026-06-27 | 139188.94 |
| 2026-06-28 | 162951.4 |
| 2026-06-29 | 122471.23 |
| 2026-06-30 | 136702.86 |
| 2026-07-01 | 135133.72 |
| 2026-07-02 | 153214.09 |
| 2026-07-03 | 163445.53 |
| 2026-07-04 | 151171.11 |
| 2026-07-05 | 161634.69 |
| 2026-07-06 | 118908.74 |
| 2026-07-07 | 144080.61 |
| 2026-07-08 | 159545.39 |
| 2026-07-09 | 161446.28 |
| 2026-07-10 | 166755.24 |
| 2026-07-11 | 116445.71 |
| 2026-07-12 | 142767.97 |
| 2026-07-13 | 146278.22 |
| 2026-07-14 | 114881.3 |
| 2026-07-15 | 162378.4 |
| 2026-07-16 | 175629.08 |
| 2026-07-17 | 145506.54 |
| 2026-07-18 | 166317.65 |
| 2026-07-19 | 146850.78 |
| 2026-07-20 | 159890.7 |
| 2026-07-21 | 173729.91 |
| 2026-07-22 | 151310.88 |
| 2026-07-23 | 170207.71 |
| 2026-07-24 | 143041.34 |
| 2026-07-25 | 140500.87 |
| 2026-07-26 | 182580.46 |
| 2026-07-27 | 171949.65 |
| 2026-07-28 | 164234.58 |
| 2026-07-29 | 130201.62 |
| 2026-07-30 | 140414.55 |
| 2026-07-31 | 151364.01 |
| 2026-08-01 | 117896.48 |
| 2026-08-02 | 137561.45 |
| 2026-08-03 | 144158.93 |
| 2026-08-04 | 166227.14 |
| 2026-08-05 | 151324.6 |
| 2026-08-06 | 148906.9 |
| 2026-08-07 | 121350.67 |
| 2026-08-08 | 170036.59 |
| 2026-08-09 | 160152.86 |
| 2026-08-10 | 162423.32 |
| 2026-08-11 | 138888.67 |
| 2026-08-12 | 131574.48 |
| 2026-08-13 | 132627.73 |
| 2026-08-14 | 137387.98 |
| 2026-08-15 | 126554.66 |
| 2026-08-16 | 128152.27 |
| 2026-08-17 | 137748.81 |
| 2026-08-18 | 157811.0 |
| 2026-08-19 | 136346.09 |
| 2026-08-20 | 164627.76 |
| 2026-08-21 | 144913.5 |
| 2026-08-22 | 128328.24 |
| 2026-08-23 | 160953.66 |
| 2026-08-24 | 152527.59 |
| 2026-08-25 | 145096.53 |
| 2026-08-26 | 162484.56 |
| 2026-08-27 | 168505.24 |
| 2026-08-28 | 160196.67 |
| 2026-08-29 | 134486.62 |
| 2026-08-30 | 138754.31 |
| 2026-08-31 | 154397.99 |
| 2026-09-01 | 139057.19 |
| 2026-09-02 | 169776.06 |
| 2026-09-03 | 180246.79 |
| 2026-09-04 | 164957.08 |
| 2026-09-05 | 152326.35 |
| 2026-09-06 | 147909.28 |
| 2026-09-07 | 182268.52 |
| 2026-09-08 | 165829.86 |
| 2026-09-09 | 114255.87 |
| 2026-09-10 | 146519.29 |
| 2026-09-11 | 196583.18 |
| 2026-09-12 | 172408.3 |
| 2026-09-13 | 148124.46 |
| 2026-09-14 | 142870.5 |
| 2026-09-15 | 191772.68 |
| 2026-09-16 | 132670.58 |
| 2026-09-17 | 130092.93 |
| 2026-09-18 | 144253.82 |
| 2026-09-19 | 123139.06 |
| 2026-09-20 | 0.0 |
| 2026-09-21 | 0.0 |
| 2026-09-22 | 0.0 |
| 2026-09-23 | 0.0 |
| 2026-09-24 | 0.0 |
| 2026-09-25 | 0.0 |
| 2026-09-26 | 0.0 |
| 2026-09-27 | 0.0 |
| 2026-09-28 | 0.0 |
| 2026-09-29 | 0.0 |
| 2026-09-30 | 0.0 |
| 2026-10-01 | 0.0 |

### Definisi metrik dari mesin

- Tabel KPI eksekutif menyediakan metrik pendapatan bersih harian.

### Peringatan dari mesin

Tidak ada yang dikembalikan oleh API untuk queri ini.

### Visualisasi yang dikembalikan oleh mesin
```json
{
  "kind": "line",
  "title": "What was the daily net revenue? — trend",
  "x": "metric_date",
  "y": [
    "net_revenue"
  ],
  "color": null
}
```

## Batasan Interpretasi

Peringatan queri di atas adalah bidang respons API, terpisah dari pemeriksaan kualitas pipeline. Queri yang berhasil tidak menghapus keterbukaan pipeline mengenai pesanan tanpa item yang diterima, cakupan inventaris yang tidak lengkap, atau perkiraan unit yang dikembalikan (refunded units).

Berkut ini adalah file bukti eksekusi queri. Airflow didokumentasikan secara terpisah di airflow_run.png.
