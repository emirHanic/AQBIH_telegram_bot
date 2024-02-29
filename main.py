import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, CallbackQueryHandler

#Import scrapers
import fhmzbih_scraper, rhmzrs_scraper

# Load environment variables from the .env file, searching up parent directories
load_dotenv()

# Access environment variables using os.environ
TOKEN = os.environ.get('TOKEN')
BOT_USERNAM = os.environ.get('BOT_USERNAME')


#COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Zdravo! Ja sam AQBiH Bot. Sve informacije o kvalitetu zraka možete pronaći ovdje.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ja sam pomocni bot.')

#Sarajevo
async def sarajevo_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Kantonu Sarajevo je:\n
        Bjelave: {fhmzbih_scraper.Sarajevo().bjelave_pm10} µg/m3\n
        Ivan Sedlo: {fhmzbih_scraper.Sarajevo().ivan_sedlo_pm10} µg/m3\n
        Vijećnica: {fhmzbih_scraper.Sarajevo().vijecnica_pm10} µg/m3\n
        Otoka: {fhmzbih_scraper.Sarajevo().otoka_pm10} µg/m3\n
        Ilidža: {fhmzbih_scraper.Sarajevo().ilidza_pm10} µg/m3\n
        Vogošća: {fhmzbih_scraper.Sarajevo().vogosca_pm10} µg/m3\n
        Hadžići: {fhmzbih_scraper.Sarajevo().hadzici_pm10} µg/m3\n
        Ilijaš: {fhmzbih_scraper.Sarajevo().ilijas_pm10} µg/m3
                                    ''')

async def sarajevo_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Kantonu Sarajevo je:\n
        Bjelave: {fhmzbih_scraper.Sarajevo().bjelave_pm25} µg/m3\n
        Ivan Sedlo: {fhmzbih_scraper.Sarajevo().ivan_sedlo_pm25} µg/m3\n
        Vijećnica: {fhmzbih_scraper.Sarajevo().vijecnica_pm25} µg/m3\n
        Otoka: {fhmzbih_scraper.Sarajevo().otoka_pm25} µg/m3\n
        Ilidža: {fhmzbih_scraper.Sarajevo().ilidza_pm25} µg/m3\n
        Vogošća: {fhmzbih_scraper.Sarajevo().vogosca_pm25} µg/m3\n
        Hadžići: {fhmzbih_scraper.Sarajevo().hadzici_pm25} µg/m3\n
        Ilijaš: {fhmzbih_scraper.Sarajevo().ilijas_pm25} µg/m3
                                    ''')

#Kakanj
async def kakanj_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Kaknju je:\n
        Doboj: {fhmzbih_scraper.Kakanj().doboj_pm10} µg/m3
                                    ''')

async def kakanj_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Kaknju je:\n
        Doboj: {fhmzbih_scraper.Kakanj().doboj_pm25} µg/m3
                                    ''')

#Jajce
async def jajce_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Jajcu je:\n
        Harmani: {fhmzbih_scraper.Jajce().harmani_pm10} µg/m3
                                    ''')

async def jajce_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Jajcu je:\n
        Harmani: {fhmzbih_scraper.Jajce().harmani_pm25} µg/m3
                                    ''')

#Travnik
async def travnik_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Travniku je:\n
        Centar: {fhmzbih_scraper.Travnik().centar_pm10} µg/m3
                                    ''')

async def travnik_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Travniku je:\n
        Centar: {fhmzbih_scraper.Travnik().centar_pm25} µg/m3
                                    ''')

#Livno
async def livno_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Livnu je:\n
        Centar: {fhmzbih_scraper.Livno().centar_pm10} µg/m3
                                    ''')

async def livno_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Livnu je:\n
        Centar: {fhmzbih_scraper.Livno().centar_pm25} µg/m3
                                    ''')

#Bihac
async def bihac_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Bihaću je:\n
        Nova Četvrt: {fhmzbih_scraper.Bihac().nova_cetvrt_pm10} µg/m3
                                    ''')

async def bihac_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Bihaću je:\n
        Nova Četvrt: {fhmzbih_scraper.Bihac().nova_cetvrt_pm25} µg/m3
                                    ''')

#Mostar
async def mostar_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Mostaru je:\n
        Bijeli Brijeg: {fhmzbih_scraper.Mostar().bijeli_brijeg_pm10} µg/m3
                                    ''')

async def mostar_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Mostaru je:\n
        Bijeli Brijeg: {fhmzbih_scraper.Mostar().bijeli_brijeg_pm25} µg/m3
                                    ''')

#Zenica
async def zenica_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Zenici je:\n
        Bijeli Brijeg: {fhmzbih_scraper.Zenica().tetovo_pm10} µg/m3\n
        Centar: {fhmzbih_scraper.Zenica().centar_pm10} µg/m3\n
        Radakovo: {fhmzbih_scraper.Zenica().radakovo_pm10} µg/m3
                                    ''')

async def zenica_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Zenici je:\n
        Tetovo: {fhmzbih_scraper.Zenica().tetovo_pm25} µg/m3\n
        Centar: {fhmzbih_scraper.Zenica().tetovo_pm25} µg/m3\n
        Radakovo: {fhmzbih_scraper.Zenica().radakovo_pm25} µg/m3
                                    ''')
        
#Visoko
async def visoko_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Visokom je:\n
        Centar: {fhmzbih_scraper.Visoko().centar_pm10} µg/m3
                                    ''')

async def visoko_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Visokom je:\n
        Centar: {fhmzbih_scraper.Visoko().centar_pm25} µg/m3
                                    ''')
        
#Maglaj
async def maglaj_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Maglaj je:\n
        Centar: {fhmzbih_scraper.Maglaj().centar_pm10} µg/m3
                                    ''')

async def maglaj_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Maglaj je:\n
        Centar: {fhmzbih_scraper.Maglaj().centar_pm25} µg/m3
                                    ''')
        
#Tesanj
async def tesanj_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Tesanju je:\n
        Vatrogasni dom: {fhmzbih_scraper.Tesanj().vatrogasni_dom_pm10} µg/m3
                                    ''')

async def tesanj_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Tesnju je:\n
        Vatrogasni dom: {fhmzbih_scraper.Tesanj().vatrogasni_dom_pm25} µg/m3
                                    ''')

#Tuzla
async def tuzla_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Tuzli je:\n
        Trnovac: {fhmzbih_scraper.Tuzla().trnovac_pm10} µg/m3\n
        Škver: {fhmzbih_scraper.Tuzla().skver_pm10} µg/m3\n
        BKC: {fhmzbih_scraper.Tuzla().bkc_pm10} µg/m3
                                    ''')

async def tuzla_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Tuzli je:\n
        Trnovac: {fhmzbih_scraper.Tuzla().trnovac_pm25} µg/m3\n
        Škver: {fhmzbih_scraper.Tuzla().skver_pm25} µg/m3\n
        BKC: {fhmzbih_scraper.Tuzla().bkc_pm25} µg/m3
                                    ''')
        
#Visoko
async def lukavac_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Lukavac je:\n
        Centar: {fhmzbih_scraper.Lukavac().centar_pm10} µg/m3
                                    ''')

async def lukavac_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Lukavac je:\n
        Centar: {fhmzbih_scraper.Lukavac().centar_pm25} µg/m3
                                    ''')

#Banja Luka
async def banjaluka_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='BanjaLuka':
                await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Banja Luci je:\n
                Banja Luka: {entry['PM10']} µg/m3
                                    ''')

async def banjaluka_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='BanjaLuka':
                await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Banja Luci je:\n
                Banja Luka: {entry['PM25']} µg/m3
                                    ''')

#Trebinje
async def trebinje_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Trebinje':
                await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Trebinju je:\n
                Trebinje: {entry['PM10']} µg/m3
                                    ''')

async def trebinje_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Trebinje':
                await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Trebinju je:\n
                Trebinje: {entry['PM25']} µg/m3
                                    ''')

#Doboj
async def doboj_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Doboj':
                await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Doboju je:\n
                Doboj: {entry['PM10']} µg/m3
                                    ''')

async def doboj_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Doboj':
                await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Doboju je:\n
                Doboj: {entry['PM25']} µg/m3
                                    ''')

#Prijedor
async def prijedor_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Prijedor':
                await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Prijedoru je:\n
                Prijedor: {entry['PM10']} µg/m3
                                    ''')

async def prijedor_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Prijedor':
                await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Prijedoru je:\n
                Prijedor: {entry['PM25']} µg/m3
                                    ''')

#Gacko
async def gacko_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Gacko':
                await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Gacku je:\n
                Gacko: {entry['PM10']} µg/m3
                                    ''')

async def gacko_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Gacko':
                await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Gacku je:\n
                Gacko: {entry['PM25']} µg/m3
                                    ''')

#Ugljevik
async def ugljevik_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Ugljevik':
                await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Ugljevik je:\n
                Gacko: {entry['PM10']} µg/m3
                                    ''')

async def ugljevik_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Ugljevik':
                await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Ugljevik je:\n
                Ugljevik: {entry['PM25']} µg/m3
                                    ''')

#Brod
async def brod_pm10_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Brod':
                await update.message.reply_text(f'''Trenutna vrijednost PM10 čestica u Brod je:\n
                Brod: {entry['PM10']} µg/m3
                                    ''')

async def brod_pm25_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        air_quality = rhmzrs_scraper.AirQualityData()
        pm_data = air_quality.get_pm_data()
        for entry in pm_data:
            if entry['StationID']=='Brod':
                await update.message.reply_text(f'''Trenutna vrijednost PM2.5 čestica u Brod je:\n
                Brod: {entry['PM25']} µg/m3
                                    ''')

#ERROR
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Bot započinje sa radom...')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(CommandHandler('sarajevo10', sarajevo_pm10_command))
    app.add_handler(CommandHandler('sarajevo25', sarajevo_pm25_command))
    app.add_handler(CommandHandler('kakanj10', kakanj_pm10_command))
    app.add_handler(CommandHandler('kakanj25', kakanj_pm25_command))
    app.add_handler(CommandHandler('jajce10', jajce_pm10_command))
    app.add_handler(CommandHandler('jajce25', jajce_pm25_command))
    app.add_handler(CommandHandler('travnik10', travnik_pm10_command))
    app.add_handler(CommandHandler('travnik25', travnik_pm25_command))
    app.add_handler(CommandHandler('livno10', livno_pm10_command))
    app.add_handler(CommandHandler('livno25', livno_pm25_command))
    app.add_handler(CommandHandler('bihac10', bihac_pm10_command))
    app.add_handler(CommandHandler('bihac25', bihac_pm25_command))
    app.add_handler(CommandHandler('mostar10', mostar_pm10_command))
    app.add_handler(CommandHandler('mostar25', mostar_pm25_command))
    app.add_handler(CommandHandler('zenica10', zenica_pm10_command))
    app.add_handler(CommandHandler('zenica25', zenica_pm25_command))
    app.add_handler(CommandHandler('visoko10', visoko_pm10_command))
    app.add_handler(CommandHandler('visoko25', visoko_pm25_command))
    app.add_handler(CommandHandler('maglaj10', maglaj_pm10_command))
    app.add_handler(CommandHandler('magalaj25', maglaj_pm25_command))
    app.add_handler(CommandHandler('tesanj10', tesanj_pm10_command))
    app.add_handler(CommandHandler('tesanj25', tesanj_pm25_command))
    app.add_handler(CommandHandler('tuzla10', tuzla_pm10_command))
    app.add_handler(CommandHandler('tuzla25', tuzla_pm25_command))
    app.add_handler(CommandHandler('lukavac10', lukavac_pm10_command))
    app.add_handler(CommandHandler('lukavac25', lukavac_pm25_command))

    app.add_handler(CommandHandler('banjaluka10', banjaluka_pm10_command))
    app.add_handler(CommandHandler('banjaluka25', banjaluka_pm25_command))
    app.add_handler(CommandHandler('trebinje10', trebinje_pm10_command))
    app.add_handler(CommandHandler('trebinje25', trebinje_pm25_command))
    app.add_handler(CommandHandler('doboj10', doboj_pm10_command))
    app.add_handler(CommandHandler('doboj25', doboj_pm25_command))
    app.add_handler(CommandHandler('prijedor10', prijedor_pm10_command))
    app.add_handler(CommandHandler('prijedor25', prijedor_pm25_command))
    app.add_handler(CommandHandler('gacko10', gacko_pm10_command))
    app.add_handler(CommandHandler('gacko25', gacko_pm25_command))
    app.add_handler(CommandHandler('ugljevik10', ugljevik_pm10_command))
    app.add_handler(CommandHandler('ugljevik25', ugljevik_pm25_command))
    app.add_handler(CommandHandler('brod10', brod_pm10_command))
    app.add_handler(CommandHandler('brod25', brod_pm25_command))

    print('Polling...')
    app.run_polling(poll_interval=3)