from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import Metashape
import random

class Ui_MainWindow(object):
    
    doc = Metashape.app.document
    chunk = Metashape.app.document.chunk
    folder_path = ""

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 698)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cam_acc_m_cb = QDoubleSpinBox(self.centralwidget)
        self.cam_acc_m_cb.setObjectName(u"cam_acc_m_cb")
        self.cam_acc_m_cb.setGeometry(QRect(240, 260, 181, 22))
        self.point_cl_qual_label = QComboBox(self.centralwidget)
        self.point_cl_qual_label.addItem("")
        self.point_cl_qual_label.addItem("")
        self.point_cl_qual_label.addItem("")
        self.point_cl_qual_label.addItem("")
        self.point_cl_qual_label.addItem("")
        self.point_cl_qual_label.setObjectName(u"point_cl_qual_label")
        self.point_cl_qual_label.setGeometry(QRect(690, 430, 181, 22))
        self.marker_acc_label = QLabel(self.centralwidget)
        self.marker_acc_label.setObjectName(u"marker_acc_label")
        self.marker_acc_label.setGeometry(QRect(40, 320, 191, 21))
        font = QFont()
        font.setPointSize(10)
        self.marker_acc_label.setFont(font)
        self.marker_acc_label.setLayoutDirection(Qt.LeftToRight)
        self.marker_acc_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.source_mod_cb = QComboBox(self.centralwidget)
        self.source_mod_cb.addItem("")
        self.source_mod_cb.addItem("")
        self.source_mod_cb.addItem("")
        self.source_mod_cb.setObjectName(u"source_mod_cb")
        self.source_mod_cb.setGeometry(QRect(240, 460, 241, 22))
        self.cam_acc_deg_label = QLabel(self.centralwidget)
        self.cam_acc_deg_label.setObjectName(u"cam_acc_deg_label")
        self.cam_acc_deg_label.setGeometry(QRect(30, 290, 201, 21))
        self.cam_acc_deg_label.setFont(font)
        self.cam_acc_deg_label.setLayoutDirection(Qt.LeftToRight)
        self.cam_acc_deg_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.measure_acc_label = QLabel(self.centralwidget)
        self.measure_acc_label.setObjectName(u"measure_acc_label")
        self.measure_acc_label.setGeometry(QRect(20, 230, 211, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.measure_acc_label.setFont(font1)
        self.measure_acc_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.marker_acc_pix_label = QLabel(self.centralwidget)
        self.marker_acc_pix_label.setObjectName(u"marker_acc_pix_label")
        self.marker_acc_pix_label.setGeometry(QRect(470, 260, 211, 21))
        self.marker_acc_pix_label.setFont(font)
        self.marker_acc_pix_label.setLayoutDirection(Qt.LeftToRight)
        self.marker_acc_pix_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scale_acc_label = QLabel(self.centralwidget)
        self.scale_acc_label.setObjectName(u"scale_acc_label")
        self.scale_acc_label.setGeometry(QRect(20, 350, 211, 21))
        self.scale_acc_label.setFont(font)
        self.scale_acc_label.setLayoutDirection(Qt.LeftToRight)
        self.scale_acc_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cam_acc_m_label = QLabel(self.centralwidget)
        self.cam_acc_m_label.setObjectName(u"cam_acc_m_label")
        self.cam_acc_m_label.setGeometry(QRect(10, 260, 221, 21))
        self.cam_acc_m_label.setFont(font)
        self.cam_acc_m_label.setLayoutDirection(Qt.LeftToRight)
        self.cam_acc_m_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tie_acc_label = QLabel(self.centralwidget)
        self.tie_acc_label.setObjectName(u"tie_acc_label")
        self.tie_acc_label.setGeometry(QRect(440, 290, 241, 21))
        self.tie_acc_label.setFont(font)
        self.tie_acc_label.setLayoutDirection(Qt.LeftToRight)
        self.tie_acc_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.photo_label = QLabel(self.centralwidget)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setGeometry(QRect(50, 70, 171, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.photo_label.setFont(font2)
        self.quality_label = QLabel(self.centralwidget)
        self.quality_label.setObjectName(u"quality_label")
        self.quality_label.setGeometry(QRect(520, 420, 161, 41))
        self.quality_label.setFont(font1)
        self.quality_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.surface_mod_cb = QComboBox(self.centralwidget)
        self.surface_mod_cb.addItem("")
        self.surface_mod_cb.addItem("")
        self.surface_mod_cb.setObjectName(u"surface_mod_cb")
        self.surface_mod_cb.setGeometry(QRect(240, 490, 241, 22))
        self.poit_cloud_label = QLabel(self.centralwidget)
        self.poit_cloud_label.setObjectName(u"poit_cloud_label")
        self.poit_cloud_label.setGeometry(QRect(520, 390, 421, 31))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.poit_cloud_label.setFont(font3)
        self.notices_label = QLabel(self.centralwidget)
        self.notices_label.setObjectName(u"notices_label")
        self.notices_label.setGeometry(QRect(610, 70, 191, 16))
        self.notices_label.setFont(font1)
        self.face_mod_label = QLabel(self.centralwidget)
        self.face_mod_label.setObjectName(u"face_mod_label")
        self.face_mod_label.setGeometry(QRect(90, 550, 141, 21))
        self.face_mod_label.setFont(font)
        self.face_mod_label.setLayoutDirection(Qt.LeftToRight)
        self.face_mod_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.coord_label = QLabel(self.centralwidget)
        self.coord_label.setObjectName(u"coord_label")
        self.coord_label.setGeometry(QRect(30, 150, 201, 21))
        self.coord_label.setFont(font1)
        self.coord_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.model_label = QLabel(self.centralwidget)
        self.model_label.setObjectName(u"model_label")
        self.model_label.setGeometry(QRect(40, 390, 361, 31))
        self.model_label.setFont(font3)
        self.general_label = QLabel(self.centralwidget)
        self.general_label.setObjectName(u"general_label")
        self.general_label.setGeometry(QRect(70, 430, 161, 21))
        self.general_label.setFont(font1)
        self.general_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.source_mod_label = QLabel(self.centralwidget)
        self.source_mod_label.setObjectName(u"source_mod_label")
        self.source_mod_label.setGeometry(QRect(90, 460, 141, 21))
        self.source_mod_label.setFont(font)
        self.source_mod_label.setLayoutDirection(Qt.LeftToRight)
        self.source_mod_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(40, 0, 821, 71))
        font4 = QFont()
        font4.setPointSize(33)
        font4.setBold(True)
        font4.setWeight(75)
        self.title_label.setFont(font4)
        self.img_coord_acc_label = QLabel(self.centralwidget)
        self.img_coord_acc_label.setObjectName(u"img_coord_acc_label")
        self.img_coord_acc_label.setGeometry(QRect(390, 230, 331, 21))
        self.img_coord_acc_label.setFont(font1)
        self.img_coord_acc_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qual_mod_cb = QComboBox(self.centralwidget)
        self.qual_mod_cb.addItem("")
        self.qual_mod_cb.addItem("")
        self.qual_mod_cb.addItem("")
        self.qual_mod_cb.addItem("")
        self.qual_mod_cb.addItem("")
        self.qual_mod_cb.setObjectName(u"qual_mod_cb")
        self.qual_mod_cb.setGeometry(QRect(240, 520, 241, 22))
        self.files_but = QPushButton(self.centralwidget)
        self.files_but.setObjectName(u"files_but")
        self.files_but.setGeometry(QRect(210, 70, 361, 31))
        self.files_but.clicked.connect(self.add_photos)
        self.surface_mod_label = QLabel(self.centralwidget)
        self.surface_mod_label.setObjectName(u"surface_mod_label")
        self.surface_mod_label.setGeometry(QRect(90, 490, 141, 21))
        self.surface_mod_label.setFont(font)
        self.surface_mod_label.setLayoutDirection(Qt.LeftToRight)
        self.surface_mod_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.face_mod_cb = QComboBox(self.centralwidget)
        self.face_mod_cb.addItem("")
        self.face_mod_cb.addItem("")
        self.face_mod_cb.addItem("")
        self.face_mod_cb.setObjectName(u"face_mod_cb")
        self.face_mod_cb.setGeometry(QRect(240, 550, 241, 22))
        self.qual_mod_label = QLabel(self.centralwidget)
        self.qual_mod_label.setObjectName(u"qual_mod_label")
        self.qual_mod_label.setGeometry(QRect(90, 520, 141, 21))
        self.qual_mod_label.setFont(font)
        self.qual_mod_label.setLayoutDirection(Qt.LeftToRight)
        self.qual_mod_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.coord_cb = QComboBox(self.centralwidget)
        self.coord_cb.addItem("")
        self.coord_cb.addItem("")
        self.coord_cb.setObjectName(u"coord_cb")
        self.coord_cb.setGeometry(QRect(240, 150, 331, 22))
        self.notices_box = QTextEdit(self.centralwidget)
        self.notices_box.setObjectName(u"notices_box")
        self.notices_box.setGeometry(QRect(610, 90, 261, 111))
        self.notices_box.setReadOnly(True)
        # connect to redirector
        sys.stdout = TextRedirector(self.notices_box)
        self.cam_acc_deg_cb = QDoubleSpinBox(self.centralwidget)
        self.cam_acc_deg_cb.setObjectName(u"cam_acc_deg_cb")
        self.cam_acc_deg_cb.setGeometry(QRect(240, 290, 181, 22))
        self.scale_acc_cb = QDoubleSpinBox(self.centralwidget)
        self.scale_acc_cb.setObjectName(u"scale_acc_cb")
        self.scale_acc_cb.setGeometry(QRect(240, 350, 181, 22))
        self.ref_sett_label = QLabel(self.centralwidget)
        self.ref_sett_label.setObjectName(u"ref_sett_label")
        self.ref_sett_label.setGeometry(QRect(30, 110, 311, 31))
        self.ref_sett_label.setFont(font3)
        self.marker_acc_pix_cb = QDoubleSpinBox(self.centralwidget)
        self.marker_acc_pix_cb.setObjectName(u"marker_acc_pix_cb")
        self.marker_acc_pix_cb.setGeometry(QRect(690, 260, 181, 22))
        self.tie_acc_cb = QDoubleSpinBox(self.centralwidget)
        self.tie_acc_cb.setObjectName(u"tie_acc_cb")
        self.tie_acc_cb.setGeometry(QRect(690, 290, 181, 22))
        
        self.targets_label = QLabel(self.centralwidget)
        self.targets_label.setObjectName(u"targets_label")
        self.targets_label.setGeometry(QRect(40, 580, 561, 31))
        self.targets_label.setFont(font3)
        self.tagets_button = QPushButton(self.centralwidget)
        self.tagets_button.setObjectName(u"tagets_button")
        self.tagets_button.setGeometry(QRect(160, 620, 261, 41))
        self.tagets_button.clicked.connect(self.detect_cross_markers)
        self.refference_button = QPushButton(self.centralwidget)
        self.refference_button.setObjectName(u"refference_button")
        self.refference_button.setGeometry(QRect(590, 340, 201, 28))
        self.refference_button.clicked.connect(self.set_reference_settings)
        self.ok_button = QPushButton(self.centralwidget)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(600, 490, 241, 61))
        self.ok_button.clicked.connect(self.final_result)
        self.marker_acc_cb = QPlainTextEdit(self.centralwidget)
        self.marker_acc_cb.setObjectName(u"marker_acc_cb")
        self.marker_acc_cb.setGeometry(QRect(240, 320, 181, 21))
        self.save_marker_button = QPushButton(self.centralwidget)
        self.save_marker_button.setObjectName(u"save_marker_button")
        self.save_marker_button.setGeometry(QRect(490, 620, 261, 41))
        self.save_marker_button.clicked.connect(self.save_markers)
    

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.point_cl_qual_label.setItemText(0, QCoreApplication.translate("MainWindow", u"1 - Ultra High", None))
        self.point_cl_qual_label.setItemText(1, QCoreApplication.translate("MainWindow", u"2 - High", None))
        self.point_cl_qual_label.setItemText(2, QCoreApplication.translate("MainWindow", u"3 - Medium", None))
        self.point_cl_qual_label.setItemText(3, QCoreApplication.translate("MainWindow", u"4 - Low", None))
        self.point_cl_qual_label.setItemText(4, QCoreApplication.translate("MainWindow", u"5 - Lowest", None))

        self.marker_acc_label.setText(QCoreApplication.translate("MainWindow", u"Marker accuracy (m):", None))
        self.source_mod_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Point cloud", None))
        self.source_mod_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Tie points", None))
        self.source_mod_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"Depth maps", None))

        self.cam_acc_deg_label.setText(QCoreApplication.translate("MainWindow", u"Camera accuracy (deg):", None))
        self.measure_acc_label.setText(QCoreApplication.translate("MainWindow", u"Measurment Accuracy:", None))
        self.marker_acc_pix_label.setText(QCoreApplication.translate("MainWindow", u"Marker accuracy (pix):", None))
        self.scale_acc_label.setText(QCoreApplication.translate("MainWindow", u"Scale bar accuracy (m):", None))
        self.cam_acc_m_label.setText(QCoreApplication.translate("MainWindow", u"Camera accuracy (m):", None))
        self.tie_acc_label.setText(QCoreApplication.translate("MainWindow", u"Tie point accuracy (pix):", None))
        self.photo_label.setText(QCoreApplication.translate("MainWindow", u"Photos folder:", None))
        self.quality_label.setText(QCoreApplication.translate("MainWindow", u"Quality:", None))
        self.surface_mod_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Arbitary (3D)", None))
        self.surface_mod_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Height field (2.5D)", None))

        self.poit_cloud_label.setText(QCoreApplication.translate("MainWindow", u"Data for building Point Cloud:", None))
        self.notices_label.setText(QCoreApplication.translate("MainWindow", u"Notices:", None))
        self.face_mod_label.setText(QCoreApplication.translate("MainWindow", u"Face count:", None))
        self.coord_label.setText(QCoreApplication.translate("MainWindow", u"Coordinate system:", None))
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"Data for building Model:", None))
        self.general_label.setText(QCoreApplication.translate("MainWindow", u"General:", None))
        self.source_mod_label.setText(QCoreApplication.translate("MainWindow", u"Source data:", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Cloud Point, Model, Targets Tool", None))
        self.img_coord_acc_label.setText(QCoreApplication.translate("MainWindow", u"Image Coordinates Accuracy:", None))
        self.qual_mod_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"1 - Ultra High", None))
        self.qual_mod_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"2 - High", None))
        self.qual_mod_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"3 - Medium", None))
        self.qual_mod_cb.setItemText(3, QCoreApplication.translate("MainWindow", u"4 - Low", None))
        self.qual_mod_cb.setItemText(4, QCoreApplication.translate("MainWindow", u"5 - Lowest", None))

        self.files_but.setText(QCoreApplication.translate("MainWindow", u"Files . . .", None))
        self.surface_mod_label.setText(QCoreApplication.translate("MainWindow", u"Surface type:", None))
        self.face_mod_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"High", None))
        self.face_mod_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.face_mod_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"Low", None))

        self.qual_mod_label.setText(QCoreApplication.translate("MainWindow", u"Quality:", None))
        self.coord_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"ETRF2000-PL / CS92 (EPSG: 2180)", None))
        self.coord_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"WGS 84 (EPSG: 4326)", None))

        self.ref_sett_label.setText(QCoreApplication.translate("MainWindow", u"Reference Settings:", None))
        self.targets_label.setText(QCoreApplication.translate("MainWindow", u"Detect Cross Non-Coded Targets:", None))
        self.tagets_button.setText(QCoreApplication.translate("MainWindow", u"DETECT", None))
        self.refference_button.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.ok_button.setText(QCoreApplication.translate("MainWindow", u"BUILD AND SAVE", None))
        self.save_marker_button.setText(QCoreApplication.translate("MainWindow", u"SAVE CAM DATA", None))
    # retranslateUi



    def add_photos(self):
        try:
            self.doc = Metashape.app.document
            self.chunk = self.doc.chunk
            self.chunk.remove(self.chunk.cameras)
            # open file dialog
            file_names = QFileDialog.getOpenFileNames(None, 'Open file', '', 'Images (*.jpg *.jpeg *.png *.tif *.tiff)')[0]
            # get path to the folder
            # print(file_names)
            print('Adding photos...')
            self.folder_path = file_names[0].rsplit('/', 1)[0] 
            # add photos to the chunk
            for file_name in file_names:
                self.chunk.addPhotos([file_name])
            print('All photos added successfully!')

            self.chunk.matchPhotos(downscale=5)
            self.chunk.alignCameras()
            self.chunk.optimizeCameras()

            print('Cameras aligned successfully!')
        except Exception as e:
            #  if list index out of range continue
            if 'list index out of range' in str(e):
                pass
            else: print(f"Error while adding photos or aligning cameras: {e}")


    def final_result(self):
        try:
            self.doc = Metashape.app.document
            self.chunk = self.doc.chunk
            self.set_reference_settings()
            # print('Reference settings done!')
            self.create_point_cloud()
            self.create_model()
        except Exception as e:
            print(f"Error in final_result: {e}")

    def set_reference_settings(self):
        try:
            self.doc = Metashape.app.document
            self.chunk = self.doc.chunk
            # coordinate system
            coord_cb = self.coord_cb.currentText()
            if coord_cb == "ETRF2000-PL / CS92 (EPSG: 2180)":
                crs_prev = self.chunk.crs
                crs_good = Metashape.CoordinateSystem("EPSG::2180")
                if crs_prev != crs_good:
                    for camera in self.chunk.cameras:
                        camera.reference.location = Metashape.CoordinateSystem.transform(camera.reference.location, crs_prev, crs_good)
                    if self.chunk.markers is not None:
                        T = self.chunk.transform.matrix
                        for marker in self.chunk.markers:
                            coord = marker.position
                            out = crs_good.project(T.mulp(coord))
                            marker.reference.location = out
                self.chunk.crs = Metashape.CoordinateSystem("EPSG::2180")

            else:
                crs_prev = self.chunk.crs
                crs_good = Metashape.CoordinateSystem("EPSG::4326")
                if crs_prev != crs_good:
                    for camera in self.chunk.cameras:
                        camera.reference.location = Metashape.CoordinateSystem.transform(camera.reference.location, crs_prev, crs_good)
                    if self.chunk.markers is not None:
                        T = self.chunk.transform.matrix
                        for marker in self.chunk.markers:
                            coord = marker.position
                            out = crs_good.project(T.mulp(coord))
                            marker.reference.location = out
                self.chunk.crs = Metashape.CoordinateSystem("EPSG::4326")
            

            # camera accuracy (meters)
            cam_acc_m_cb = self.cam_acc_m_cb.value()
            if cam_acc_m_cb == "":
                cam_acc_m_cb = 10
            self.chunk.camera_location_accuracy = Metashape.Vector([cam_acc_m_cb, cam_acc_m_cb, cam_acc_m_cb])

            # camera accuracy (degrees)
            cam_acc_deg_cb = self.cam_acc_deg_cb.value()
            self.chunk.camera_rotation_accuracy = Metashape.Vector([cam_acc_deg_cb, cam_acc_deg_cb, cam_acc_deg_cb])

            # marker accuracy (meters)
            marker_acc_cb = self.marker_acc_cb.toPlainText()
            # self.chunk.marker_location_accuracy = Metashape.Vector([marker_acc_cb, marker_acc_cb, marker_acc_cb])
            if marker_acc_cb == "":
                marker_acc_cb = 0
            elif '/' in marker_acc_cb:
                num = []
                for i in marker_acc_cb.split('/'):
                    num.append(float(i))
                self.chunk.marker_location_accuracy = Metashape.Vector(num)
            else:
                self.chunk.marker_location_accuracy = Metashape.Vector([float(marker_acc_cb), float(marker_acc_cb), float(marker_acc_cb)])

            # scale bar accuracy (meters)
            scale_acc_cb = self.scale_acc_cb.value()
            self.chunk.scalebar_accuracy = scale_acc_cb

            # marker accuracy (pixels)
            marker_acc_pix_cb = self.marker_acc_pix_cb.value()
            self.chunk.marker_projection_accuracy = marker_acc_pix_cb

            # tie point accuracy (pixels)
            tie_acc_cb = self.tie_acc_cb.value()
            self.chunk.tiepoint_accuracy = tie_acc_cb
            print('Reference settings set successfully!')
        except Exception as e:
            print(f"Error while reference setting: {e}")

    def create_point_cloud(self):
        try:
            print('Creating point cloud...')
            # quality
            point_cl_qual_label =self.point_cl_qual_label.currentText()
            if point_cl_qual_label == "1 - Ultra High":
                num = 1
            elif point_cl_qual_label == "2 - High":
                num = 2
            elif point_cl_qual_label == "3 - Medium":
                num = 4
            elif point_cl_qual_label == "4 - Low":
                num = 8
            else:
                num = 16
            self.chunk.buildDepthMaps(downscale=num, filter_mode=Metashape.MildFiltering)
            self.chunk.buildPointCloud()
            print('Point cloud created successfully!')
            num = random.randint(1, 9999)
            self.chunk.exportPointCloud(self.folder_path + '/point_cloud' + str(num) + '.las')
            print(f'Point cloud saved successfully in folder: {self.folder_path}/point_cloud{num}.las!')
        except Exception as e:
            print(f"Error while creating point cloud: {e}")

    def create_model(self):
        try:
            print('Creating model...')
            source_data = self.source_mod_cb.currentText()
            if source_data == "Point cloud":
                source_data = Metashape.PointCloudData
            elif source_data == "Tie points":
                source_data = Metashape.TiePointsData
            else:
                source_data = Metashape.DepthMapsData

            if source_data in [Metashape.PointCloudData, Metashape.TiePointsData]:
                surface_type = self.surface_mod_cb.currentText()
                if surface_type == "Arbitrary (3D)":
                    surface_type = Metashape.Arbitrary
                else:
                    surface_type = Metashape.HeightField
            else:
                surface_type = Metashape.Arbitrary

            if source_data == Metashape.DepthMapsData:
                quality = self.qual_mod_cb.currentText()
                if quality == "1 - Ultra High":
                    quality = 1
                elif quality == "2 - High":
                    quality = 2
                elif quality == "3 - Medium":
                    quality = 4
                elif quality == "4 - Low":
                    quality = 8
                else:
                    quality = 16
                self.chunk.buildDepthMaps(downscale=quality, filter_mode=Metashape.MildFiltering)

            face_count = self.face_mod_cb.currentText()
            if face_count == "High":
                face_count = Metashape.HighFaceCount
            elif face_count == "Medium":
                face_count = Metashape.MediumFaceCount
            else:
                face_count = Metashape.LowFaceCount
            self.chunk.buildModel(surface_type=surface_type, source_data=source_data, face_count=face_count)
            num = random.randint(1, 9999)
            print('Model created successfully!')
            self.chunk.exportModel(self.folder_path + '/model' + str(num) + '.obj')
            print(f'Model saved successfully in folder: {self.folder_path}/model{num}.obj!')

        except Exception as e:
            print(f"Error while building model: {e}")

    def detect_cross_markers(self):
        try: 
            print('Detecting cross markers...')
            self.doc = Metashape.app.document
            self.chunk = self.doc.chunk
            marker_type = Metashape.TargetType.CrossTarget
            self.chunk.detectMarkers(target_type=marker_type, tolerance = 0)
            for marker in self.chunk.markers:
                coord = marker.position
                marker.label = 'DT' + str(marker.label)
                marker.reference.location = coord
            self.set_reference_settings()
            self.set_reference_settings()
            print('Cross markers detected successfully!')
            self.chunk.matchPhotos(downscale=5)
            self.chunk.alignCameras()
            self.chunk.optimizeCameras()
            print('Cameras realigned successfully!')
            self.save_markers()

        except Exception as e:
            print(f"Error while detecting cross markers: {e}")


    def save_markers(self):
        try:
            self.doc = Metashape.app.document
            self.chunk = self.doc.chunk
            if self.folder_path == "":
                # get folder path from first camera
                self.folder_path = self.chunk.cameras[0].photo.path.rsplit('/', 1)[0]
            num = random.randint(1, 9999)
            file_name = self.folder_path + '/markers' + str(num) + '.txt'
            file = open(file_name, 'w')
            #  write coordinate system
            file.write(f'Coordinate system: {self.chunk.crs}\n')
            file.write('label,x,y,h,yaw,pitch,roll\n')
            for camera in self.chunk.cameras:
                file.write(f'{camera.label},{camera.reference.location.x},{camera.reference.location.y},{camera.reference.location.z},{camera.reference.rotation.x},{camera.reference.rotation.y},{camera.reference.rotation.z}\n')
            file.close()
            print(f'Markers saved successfully: {file_name}!')
        except Exception as e:
            print(f"Error while saving markers: {e}")


class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, message):
        self.widget.setReadOnly(False)
        self.widget.append(message)
        self.widget.setReadOnly(True)
        sys.__stdout__.write(message)  # Also write to the terminal

    def flush(self):
        pass


class Wizard(QDialog, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wizard")
        # self.setGeometry(100, 100, 400, 300)
        # self.layout = QVBoxLayout()
        # self.setLayout(self.layout)
        self.setupUi(self)

def build_model_and_cloud_point_tool():
    try:
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        wizard = Wizard()
        print('Wizard created!')

        wizard.exec_()
        wizard.show()
    except Exception as e:
        print(f"Error in build_model_and_cloud_point_tool: {e}")


try:
    Metashape.app.removeMenuItem("Build Model and Cloud Point Tool")
    Metashape.app.addMenuItem("Build Model and Cloud Point Tool", build_model_and_cloud_point_tool)
except Exception as e:
    print(f"Error in menu item setup: {e}")

