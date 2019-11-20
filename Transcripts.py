def Transcripts():

    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Transcripts_MonsoonNewPadButton"))
    snooze(5)

    mouseClick(waitForObject(":Transcripts.Transcripts_LCLabel"), 29, 14, 4, Button.Button3)
    activateItem(waitForObjectItem(":Transcripts_TitlebarPanel", "Attach"))

    snooze(3)
    mouseClick(waitForObject(":Data & Analytics NYSE QA_LCTextField"), 35, 7, 0, Button.Button1)
    type(waitForObject(":Data & Analytics NYSE QA_LCTextField"), "ibm")
    type(waitForObject(":Data & Analytics NYSE QA_LCTextField"), "<Return>")
    snooze(5)
    type(waitForObject(":Data & Analytics NYSE QA_LCTextField"), "msft")
    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA_LCAppendedButton_7"))
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA_LCAppendedButton_8"))
    snooze(5)
    clickButton(waitForObject(":Symbol Lookup.Search_FixedSizeButton"))
    snooze(4)
    clickButton(waitForObject(":Symbol Lookup.OK_FixedSizeButton"))
    snooze(3)
    


    clickButton(waitForObject(":Data & Analytics NYSE QA.Symbol(s)_LCDropDownButton"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Symbol(s)_LCDropDownButton", "Active Symbols"))

    snooze(3)
    


    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_3"), 7, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Today"), 39, 14, 0, Button.Button1)

    snooze(3)
    
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", "All Events"), 7, 10, 0, Button.Button1)
    snooze(5)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_3"), 10, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Yesterday"), 73, 6, 0, Button.Button1)
    snooze(3)
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_3"), 5, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Last 7 Days"), 60, 12, 0, Button.Button1)
    snooze(3)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.Active Symbols_LCDropDownButton"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Active Symbols_LCDropDownButton", "Watch List"))
    clickButton(waitForObject(":Data & Analytics NYSE QA.Please select watch list_LCTreeButton"))
    expand(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Workspace Symbol Lists"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Workspace Symbol Lists.Dow/S&P/NYSE"), 24, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.Dow/S&P/NYSE_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Workspace Symbol Lists.Equities"), 16, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.Equities_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Workspace Symbol Lists.Futures"), 11, 9, 0, Button.Button1)
    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Futures_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Workspace Symbol Lists.Market Stats"), 29, 9, 0, Button.Button1)
    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Market Stats_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Workspace Symbol Lists.Mkt Overview"), 30, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.Mkt Overview_LCTreeButton"))
    collapse(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Workspace Symbol Lists"))
    expand(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only)"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only).Stocks"), 7, 9, 0, Button.Button1)
    snooze(5)

    clickButton(waitForObject(":Data & Analytics NYSE QA.Stocks_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only).Futures"), 19, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.Futures_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only).US"), 21, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.US_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only).Forex"), 7, 9, 0, Button.Button1)
    
    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Forex_LCTreeButton"))
    collapse(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only)"))
    expand(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.Dow Jones Industrial Average"), 35, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.Dow Jones Industrial Average_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.Dow Jones Composite Average"), 79, 9, 0, Button.Button1)
    
    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Dow Jones Composite Average_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.Dow Transportation Average"), 40, 9, 0, Button.Button1)
    
    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Dow Transportation Average_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.NASDAQ 100"), 59, 9, 0, Button.Button1)   
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.NASDAQ 100_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.NASDAQ Composite"), 97, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.NASDAQ Composite_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.S&P/TSX Composite Index"), 80, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.S&P/TSX Composite Index_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.S&P/TSX Venture Composite Index"), 93, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.S&P/TSX Venture Composite Index_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.NYSE (All)"), 49, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.NYSE (All)_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.NASDAQ (All)"), 41, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.NASDAQ (All)_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.AMEX (All)"), 64, 9, 0, Button.Button1)
    snooze(5)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.AMEX (All)_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.US (All)"), 39, 9, 0, Button.Button1)

    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.US (All)_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.Dow Jones Industrial Average"), 90, 9, 0, Button.Button1)
    snooze(5)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Dow Jones Industrial Average_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.NASDAQ 100"), 37, 9, 0, Button.Button1)
    snooze(5)
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_2"), 7, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Last 30 Days"), 48, 14, 0, Button.Button1)
    snooze(3)
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_2"), 9, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Last 12 Months"), 74, 6, 0, Button.Button1)
    snooze(5)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_2"), 8, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Upcoming Events"), 55, 13, 0, Button.Button1)
    snooze(4)

    clickButton(waitForObject(":Data & Analytics NYSE QA.Calendar_LCDropDownButton"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Calendar_LCDropDownButton", "Agenda"))
    snooze(4)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Stocks_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only).Futures"), 24, 9, 0, Button.Button1)
    snooze(4)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Futures_LCTreeButton"))
    expand(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.Dow Jones Industrial Average"), 26, 9, 0, Button.Button1)
    snooze(4)
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_2"), 5, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Last 7 Days"), 36, 13, 0, Button.Button1)
    snooze(4)
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_2"), 4, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Last 30 Days"), 36, 8, 0, Button.Button1)
    snooze(4)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Dow Jones Industrial Average_LCTreeButton"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Mobile Home Page (Phone Only).Stocks"), 35, 9, 0, Button.Button1)
    snooze(4)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Watch List_LCDropDownButton"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Watch List_LCDropDownButton", "Active Symbols"))
    snooze(4)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Agenda_LCDropDownButton"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Agenda_LCDropDownButton", "Calendar"))
    snooze(3)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Active Symbols_LCDropDownButton"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Active Symbols_LCDropDownButton", "Watch List"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_2"), 6, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Last 30 Days"), 73, 2, 0, Button.Button1)
    snooze(3)
    
    clickButton(waitForObject(":Data & Analytics NYSE QA.Stocks_LCTreeButton"))
    expand(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.Dow Jones Industrial Average"), 37, 9, 0, Button.Button1)
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 93, 52, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Hide Tree"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_4"), 54, 41, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Show Tree"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 114, 70, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Print"))
    
    snooze(3)
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_4"), 48, 73, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Display Properties..."))
    mouseClick(waitForObjectItem(":Calendar Properties.com.futuresource.livecharts.common.LCCardList$1_LCList", "Text & Colors  "), 77, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties_CommonButton"), 5, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Calendar Properties.ComboBox.list_JList", "16"), 13, 15, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 110, 41, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Defaults"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Defaults_JMenu_20", "Save Transcripts Properties As Default"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    snooze(2)
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 144, 66, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Defaults"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Defaults_JMenu_20", "Apply Default Properties to the Transcripts"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton_4"))
    snooze(3)
    clickButton(waitForObject(":Data & Analytics NYSE QA.Transcripts_MonsoonNewPadButton"))
    snooze(3)
    mouseClick(waitForObject(":Transcripts.Transcripts_LCLabel"), 28, 9, 4, Button.Button3)
    activateItem(waitForObjectItem(":Transcripts_TitlebarPanel", "Attach"))
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_5"), 85, 39, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Defaults"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Defaults_JMenu_20", "Apply Default Properties to all Transcripts Windows"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton_4"))
    clickButton(waitForObject(":Data & Analytics NYSE QA.Transcripts_MonsoonNewPadButton"))
    snooze(2)
    mouseClick(waitForObject(":Transcripts.Transcripts_LCLabel"), 35, 11, 4, Button.Button3)
    activateItem(waitForObjectItem(":Transcripts_TitlebarPanel", "Attach"))
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_5"), 105, 36, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Defaults"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Defaults_JMenu_20", "Remove Default Transcripts Properties"))
    clickButton(waitForObject(":Question.Yes_FixedSizeButton"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton_4"))
    clickButton(waitForObject(":Data & Analytics NYSE QA.Transcripts_MonsoonNewPadButton"))
    snooze(2)
    mouseClick(waitForObject(":Transcripts.Transcripts_LCLabel"), 44, 7, 4, Button.Button3)
    activateItem(waitForObjectItem(":Transcripts_TitlebarPanel", "Attach"))
    clickButton(waitForObject(":Data & Analytics NYSE QA.Symbol(s)_LCDropDownButton"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.Symbol(s)_LCDropDownButton", "Watch List"))
    clickButton(waitForObject(":Data & Analytics NYSE QA.Please select watch list_LCTreeButton"))
    expand(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists"))
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA_LCTree", ".Server Symbol Lists.Dow Jones Industrial Average"), 18, 9, 0, Button.Button1)
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_5"), 83, 1, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Display Properties..."))
    mouseClick(waitForObjectItem(":Calendar Properties.com.futuresource.livecharts.common.LCCardList$1_LCList", "General  "), 48, 4, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties.Full Week View_LCCheckBox"), 10, 11, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA_CommonButton_2"), 4, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data & Analytics NYSE QA.ComboBox.list_JList", "Last 7 Days"), 39, 11, 0, Button.Button1)
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 91, 46, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Display Properties..."))
    mouseClick(waitForObject(":Calendar Properties.Full Week View_LCCheckBox"), 9, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties.View:_CommonButton"), 10, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Calendar Properties.ComboBox.list_JList", "Agenda"), 58, 9, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA_JViewport_3"), 182, 130, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCScrollPane_LCScrollPane", "Display Properties..."))
    mouseClick(waitForObject(":Calendar Properties.View:_CommonButton"), 3, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Calendar Properties.ComboBox.list_JList", "Calendar"), 37, 16, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties.Show Side Event View_LCCheckBox"), 8, 13, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 67, 58, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Display Properties..."))
    mouseClick(waitForObject(":Calendar Properties.Show Side Event View_LCCheckBox"), 12, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Calendar Properties.com.futuresource.livecharts.common.LCCardList$1_LCList", "Calendar Event  "), 62, 4, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties. _FixedSizeButton"))
    clickButton(waitForObject(":Calendar Properties_FixedSizeButton"))
    clickButton(waitForObject(":Calendar Properties. _FixedSizeButton_2"))
    clickButton(waitForObject(":Calendar Properties_FixedSizeButton_2"))
    mouseClick(waitForObject(":Calendar Properties.Show Calendar Event in Separate Window_LCCheckBox"), 3, 9, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 64, 70, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Display Properties..."))
    mouseClick(waitForObjectItem(":Calendar Properties.com.futuresource.livecharts.common.LCCardList$1_LCList", "Text & Colors  "), 67, 6, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties_CommonButton_2"), 5, 6, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Calendar Properties.ComboBox.list_JList", "Open Sans Extrabold"), 80, 16, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties_CommonButton"), 5, 4, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Calendar Properties.ComboBox.list_JList", "14"), 9, 7, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties.Italic_LCCheckBox"), 4, 10, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties. _FixedSizeButton_3"))
    clickButton(waitForObject(":Calendar Properties_FixedSizeButton_3"))
    clickButton(waitForObject(":Calendar Properties. _FixedSizeButton_4"))
    clickButton(waitForObject(":Calendar Properties_FixedSizeButton_4"))
    clickButton(waitForObject(":Calendar Properties. _FixedSizeButton_5"))
    clickButton(waitForObject(":Calendar Properties_FixedSizeButton_5"))
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 56, 66, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Display Properties..."))
    mouseClick(waitForObjectItem(":Calendar Properties.com.futuresource.livecharts.common.LCCardList$1_LCList", "Gridlines  "), 49, 4, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties.com.futuresource.livecharts.dialogs.GridPanel$2_LCPanel"), 1, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Calendar Properties.Show Gridlines_LCCheckBox"), 6, 11, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 147, 86, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_CalendarMainDateTable", "Display Properties..."))
    mouseClick(waitForObject(":Calendar Properties.Show Gridlines_LCCheckBox"), 9, 8, 0, Button.Button1)
    clickButton(waitForObject(":Calendar Properties. _FixedSizeButton_6"))
    clickButton(waitForObject(":Calendar Properties_FixedSizeButton_6"))
    clickButton(waitForObject(":Calendar Properties.OK_FixedSizeButton"))
    snooze(3)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 20, 9, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Watch List"))
    activateItem(waitForObjectItem(":Watch List_JMenu_13", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 31, 6, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Quotes Grid"))
    activateItem(waitForObjectItem(":Quotes Grid_JMenu_10", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 29, 12, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Chart"))
    activateItem(waitForObjectItem(":Chart_JMenu_26", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 24, 10, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "News"))
    activateItem(waitForObjectItem(":News_JMenu_9", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 30, 13, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Hot Lists"))
    activateItem(waitForObjectItem(":Hot Lists_JMenu_10", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 33, 9, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Detailed Quotes"))
    activateItem(waitForObjectItem(":Detailed Quotes_JMenu_9", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 38, 9, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Alerts"))
    activateItem(waitForObjectItem(":Alerts_JMenu_9", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 37, 7, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Time & Sales"))
    activateItem(waitForObjectItem(":Time & Sales_JMenu_9", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 29, 10, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Market Depth"))
    activateItem(waitForObjectItem(":Market Depth_JMenu_9", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 47, 13, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "New"))
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA.New_JMenu_17", "Net House"))
    activateItem(waitForObjectItem(":Net House_JMenu_9", "To the right"))
    snooze(2)
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    clickButton(waitForObject(":Data & Analytics NYSE QA_JButton"))
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 20, 10, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "Show Window Title"))
    snooze(2)
    mouseClick(waitForObject(":Data & Analytics NYSE QA. _LCLabel_12"), 3, 6, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "Show Window Title"))
    snooze(2)
    test.compare(waitForObjectExists(":Data & Analytics NYSE QA.Transcripts_LCLabel").name, "Transcripts")
    
    snooze(2)
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel"), 31, 5, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "Show Titlebar description"))
    snooze(2)
    test.compare(waitForObjectExists(":Data & Analytics NYSE QA.Transcripts_LCLabel_2").text, "Transcripts")
    snooze(2)
    
    mouseClick(waitForObject(":Data & Analytics NYSE QA.Transcripts_LCLabel_2"), 26, 9, 4, Button.Button3)
    activateItem(waitForObjectItem(":Data & Analytics NYSE QA_TitlebarPanel", "Customize Titlebar Description..."))
    type(waitForObject(":Titlebar Description Settings.Transcripts_LCTextArea"), "test ")
    mouseClick(waitForObject(":Titlebar Description Settings.Foreground: _LCCheckBox"), 8, 8, 0, Button.Button1)
    clickButton(waitForObject(":Titlebar Description Settings. _FixedSizeButton"))
    clickButton(waitForObject(":Titlebar Description Settings_CommonButton"))
    mouseClick(waitForObject(":Titlebar Description Settings.Background: _LCCheckBox"), 7, 8, 0, Button.Button1)
    clickButton(waitForObject(":Titlebar Description Settings. _FixedSizeButton_2"))
    clickButton(waitForObject(":Titlebar Description Settings_FixedSizeButton_9"))
    setValue(waitForObject(":Titlebar Description Settings., Transparency: _LCSpinner"), 49)
    mouseClick(waitForObject(":Titlebar Description Settings.Font: _LCCheckBox"), 7, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Titlebar Description Settings.com.futuresource.livecharts.common.LCComboBox_LCComboBox_2"), 106, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Titlebar Description Settings.ComboBox.list_JList", "Open Sans Extrabold"), 73, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Titlebar Description Settings_CommonButton_2"), 5, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Titlebar Description Settings.ComboBox.list_JList", "14"), 9, 8, 0, Button.Button1)
    mouseClick(waitForObject(":Titlebar Description Settings.Bold_LCCheckBox"), 6, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Titlebar Description Settings.Italic_LCCheckBox"), 3, 16, 0, Button.Button1)
    clickButton(waitForObject(":Titlebar Description Settings.OK_FixedSizeButton"))

    snooze(40)
