
ria_df = pd.read_csv('/home/jonatron/noaa_out.csv', index_col='DATE', parse_dates=True)
#pv = pd.pivot_table(ria_df, index=ria_df.index.month, columns=ria_df.index.year, values='sixhoursbuffgood', aggfunc='sum')
noaastations = ['WBAN:00120', 'WBAN:00153', 'WBAN:00154', 'WBAN:00155',
       'WBAN:00274', 'WBAN:00367', 'WBAN:00416', 'WBAN:03701',
       'WBAN:03704', 'WBAN:03706', 'WBAN:03707', 'WBAN:03710',
       'WBAN:03714', 'WBAN:03715', 'WBAN:03716', 'WBAN:03717',
       'WBAN:03718', 'WBAN:03719', 'WBAN:03730', 'WBAN:03734',
       'WBAN:03735', 'WBAN:03739', 'WBAN:03759', 'WBAN:13702',
       'WBAN:13728', 'WBAN:13733', 'WBAN:13737', 'WBAN:13740',
       'WBAN:13741', 'WBAN:13743', 'WBAN:13750', 'WBAN:13762',
       'WBAN:13763', 'WBAN:13769', 'WBAN:13773', 'WBAN:13868',
       'WBAN:53818', 'WBAN:53881', 'WBAN:53895', 'WBAN:63802',
       'WBAN:63805', 'WBAN:63806', 'WBAN:93714', 'WBAN:93728',
       'WBAN:93735', 'WBAN:93736', 'WBAN:93738', 'WBAN:93739',
       'WBAN:93741', 'WBAN:93757', 'WBAN:93760', 'WBAN:93773',
       'WBAN:93775', 'WBAN:93797', 'WBAN:93798']
years = [2014, 2015, 2016, 2017, 2018]
#feature_names = ria_df.columns[0:-1].values.tolist()

def get_data_n(src, station, year):
    df = src[(src.index.year == year) & (src.STATION == station)].resample('1M').sum().copy()
    #df = src[src.STATION == station].copy()
    #df = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values='sixhoursbuffgood', aggfunc='sum')
    return ColumnDataSource(data=df)

def create_figure_n(source, current_station, current_year):
    p = figure(x_axis_type="datetime", plot_width=800)
    p.title.text = "6 hr paveable periods"
    p.line(x='DATE', y='sixhoursbuffgood', source=source)
    p.xaxis.axis_label = "Date"
    p.yaxis.axis_label = current_station
    p.axis.axis_label_text_font_style = "bold"
    p.x_range = DataRange1d(range_padding=0.0)
    p.grid.grid_line_alpha = 0.3
    return p


@app.route('/noaa')
def noaa():
    current_station = request.args.get('station')
    current_year = request.args.get('year', type = int)
    if current_station == None:
        current_station = "WBAN:00274"
    if current_year == None:
        current_year = 2014
    source = get_data_n(ria_df, current_station, current_year)
    plot = create_figure_n(source, current_station, current_year)
    script, div = components(plot)

    return render_template("noaa.html", script=script, div=div, noaastations=noaastations, current_station=current_station, years=years, current_year=current_year)
