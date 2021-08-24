from PyQt5.QtWidgets import QMainWindow
from src.Stats.Controllers.StatsManager import StatsManager
from PyQt5.uic import loadUi
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class StatsView(QMainWindow):

    def __init__(self, widget):
        super(StatsView, self).__init__()
        self.statsM = StatsManager()
        loadUi("../designer/Stats/Stats.ui", self)
        self.widget = widget
        self.load_user_fields()
        #self.loan_stats()

    def load_user_fields(self):
        user_count = self.statsM.get_user_count()
        self.n_users.setText(str(user_count))

        self.male.setText(str(round((self.statsM.get_user_count_gender('Maschio(M)') / user_count) * 100, 2)) + '%')
        self.female.setText(str(round((self.statsM.get_user_count_gender('Femmina(F)') / user_count) * 100, 2)) + '%')

        self.zero_seventeen.setText(str(round(
            (self.statsM.get_user_by_bdate(date.today(), date.today() - relativedelta(years=17)) / user_count) * 100,
            2)) + '%')
        self.eighteentfive.setText(str(round((self.statsM.get_user_by_bdate(date.today() - relativedelta(years=18),
                                                                            date.today() - relativedelta(
                                                                                years=25)) / user_count) * 100,
                                             2)) + '%')
        self.tsixfifty.setText(str(round((self.statsM.get_user_by_bdate(date.today() - relativedelta(years=26),
                                                                        date.today() - relativedelta(
                                                                            years=50)) / user_count) * 100, 2)) + '%')
        self.foneplus.setText(str(round((self.statsM.get_user_by_bdate(date.today() - relativedelta(years=50),
                                                                       date.today() - relativedelta(
                                                                           years=200)) / user_count) * 100, 2)) + '%')

    def loan_stats(self):
        pass
