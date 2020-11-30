import xlwings as xw

from common.auto_dict import _AutoDict, dict_to_object


class OperatingExcel:
    """
    ColorIndex: 0:无色,   3:红色,   36:黄色,   8:蓝色
    """

    def __init__(self, filepath, sheetname):
        self.app = xw.App(visible=False, add_book=False)
        self.app.display_alerts = False
        self.app.screen_updating = False
        self.wb = self.app.books.open(filepath)
        self.sheet = self.wb.sheets[sheetname]
        self.max_row = self.sheet.used_range.last_cell.row
        self.max_column = self.sheet.used_range.last_cell.column

    def __del__(self):
        self.wb.save()
        pass
        self.app.quit()

    def w_data(self, start_rng, data_list, if_vertical=False):
        """
        if_vertical: False:vertical,     True:horizon
        :return: None
        """
        self.sheet.range(start_rng).options(transpose=if_vertical).value = data_list

    def set_inter(self, start_rng, inter_dict):
        for attr in inter_dict.keys():
            exec(f'self.sheet.range(start_rng).api.Interior.{attr} = inter_dict["{attr}"]')

    def set_font(self, start_rng, font_dict):
        for attr in font_dict.keys():
            exec(f'self.sheet.range(start_rng).api.Font.{attr} = font_dict["{attr}"]')

    def set_common_attr(self, start_rng, table_name, table_dict):
        for attr in table_dict.keys():
            exec(f'self.sheet.range(start_rng).api.{table_name}.{attr} = table_dict["{attr}"]')

    def clear_sheet(self):
        self.sheet.clear()

    def autofit(self, type='c'):
        self.sheet.autofit(type)

    def read_titles(self, deep_sides):
        all_title = []
        temp_value = None
        for title_row in range(1, deep_sides + 1):
            contents = []
            for rng in self.sheet.range(f"{title_row}:{title_row}"):
                if rng.column > self.max_column:
                    break
                if rng.value:
                    temp_value = rng.value
                contents.append(temp_value)
            all_title.append(contents)
        return all_title

    def read_one_line(self, row):
        contents = []
        for rng in self.sheet.range(f"{row}:{row}"):
            if rng.column > self.max_column:
                break
            contents.append(rng.value)
        return contents

    def read_data_obj(self, title_deep_sides=1):
        all_cases = []
        all_title = self.read_titles(title_deep_sides)
        for data_row in range(title_deep_sides + 1, self.max_row + 1):
            data = self.read_one_line(data_row)
            dict_all = _AutoDict()
            zip_tuple = list(zip(*all_title, data))
            string = "dict_all"
            for _ in range(title_deep_sides):
                string += f"[item[{_}]]"
            string += f" = item[{_ + 1}]"
            for item in zip_tuple:
                exec(string)
            res = dict_to_object(dict_all)
            all_cases.append(res)
        for index, value in enumerate(all_cases):
            value.row = title_deep_sides + 1
            value.max_column = self.max_column
        print(all_cases)
        return all_cases


if __name__ == '__main__':
    o1 = OperatingExcel("./ALL_4.xlsx", "Sheet1")
    res = o1.read_data_obj(3)
    # o1.w_data("A1:A10", [1, 2, 3333, 4, 5], if_vertical=True)
    # o1.set_font("D3:F3", font_dict)
    # fff = MyDict()
    # fff["1"]
    # print(fff)
