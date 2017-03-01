import random
import math

def cariMean(alist):
	temp = list(alist)
	temp.sort()
	alen = len(temp)

	if(alen % 2) == 1:
		return temp[alen // 2]
	else:
		return (temp[alen // 2] + temp[(alen // 2) - 1]) / 2

def normalisasiKolom(kolom):
	mean = cariMean(kolom)
	asd = math.sqrt((sum([abs(x - mean) for x in kolom]))**2 / len(kolom))
	hasil = [(x - mean) / asd for x in kolom]

	return hasil

class KMeans:
		def __init__(self, namaFile, k):
			self.k = k
			self.populasi = []
			self.chromosome = []
			self.centroids = []
			self.sse = 0
			self.data = {}
			self.pointsChanged = 0
			self.iterationNumber = 0

			with open(namaFile) as f:
				baris = f.readlines()
				f.close()
			formatData = baris[0].split(',')
			self.kolom = len(formatData) 
			print(self.kolom)

			self.data = [[] for i in range(len(formatData))]

			for line in baris[1:]:
				fitur = line.split(',')
				kelas = 0
				count = 0
				for kolom in range(self.kolom):
					if kelas == 0:
						self.data[kolom].append(fitur[4])
						
						kelas = 1
					else:
						self.data[kolom].append(float(fitur[count]))
						count +=1
						
			
			print("data ke 1", self.data[1])
			print("kolom", self.kolom)

			self.jumlahData = len(self.data[1])
			self.memberOf = [-1 for x in range(len(self.data[1]))]

			print("member of atas", self.memberOf)

			print("Self data before: ", self.data)

			"""for i in range(1, self.kolom):
				self.data[i] = normalisasiKolom(self.data[i])"""

			print("self data after: ", self.data)

			random.seed()
			c1 = random.sample(range(1,50),1)
			print("c1: ", c1)
			c2 = random.sample(range(51,100),1)
			print("c2: ", c2)
			c3 = random.sample(range(101, 150),1)
			print("c3: ", c3)
			centro1 = []

			centro1 = [self.data[i][r] for i in range(1, len(self.data))
						for r in c1]
			centro2 = [self.data[i][r] for i in range(1, len(self.data))
						for r in c2]
			centro3 = [self.data[i][r] for i in range(1, len(self.data))
						for r in c3]
			#self.centroids = centroid
			"""self.centroids = []
			self.centroids.append(centro1)
			self.centroids.append(centro2)
			self.centroids.append(centro3)"""
			"""self.centroids = [[self.data[i][r] for i in range(1,len(self.data))]
								for r in nomor: for y in r]"""
			"""self.centroids = [[self.data[i][r] for i in range(1, len(self.data))]
								for r in random.sample(range(len(self.data[0])), self.k)]"""
			#self.centroids = [[self.data[1][r]] for r in random.sample(range(len(self.data[0]), self.k))]
			#self.make_populasi()
			#self.evaluasi_populasi()
			#print("Self Centroids", self.centroids)

			#self.masukanVectorKeCluster()

		"""def make_populasi(self):
			self.populasi = []
			c1 = 0
			c2 = 50
			c3 = 100

			for x in range(0, 50): #population sizenya 50
				self.chromosome = []
				
				genotipe1 = [self.data[i][c1] for i in range(1, len(self.data))]
				genotipe2 = [self.data[i][c2] for i in range(1, len(self.data))]
				genotipe3 = [self.data[i][c3] for i in range(1, len(self.data))]
				self.chromosome.append(genotipe1)
				self.chromosome.append(genotipe2)
				self.chromosome.append(genotipe3)
				self.populasi.append(self.chromosome)
				
				c1+=1
				c2+=1
				c3+=1
			print("Populasi: ", self.populasi)

		def evaluasi_populasi(self):
			self.centroids = self.populasi[21]"""

							
							

		def updateCentroids(self):
			print("Update Centroids")
			members = [self.memberOf.count(i) for i in range(len(self.centroids))]
			self.centroids = [[sum([self.data[k][i] 
									for i in range(len(self.data[0]))
									if self.memberOf[i] == centroid])/members[centroid]
									for k in range(1, len(self.data))]
									for centroid in range(len(self.centroids))]
			print("Members di update centroid ", members)
			print("Centroid di update centroid ", self.centroids)

		def masukanVectorKeClusterBerdasarCentroid(self, i):
			#berdasar jarak ke centroid
			minimum = 999999 #infinity
			clusterNomor = -1

			for centroid in range(self.k):
				jarak = self.EucledianDistance(i, centroid)

				if jarak < minimum:
					minimum = jarak
					clusterNomor = centroid

			if clusterNomor != self.memberOf[i]:
				self.pointsChanged += 1

			self.sse+=minimum**2
			
			return clusterNomor

		def masukanVectorKeCluster(self):
			self.pointsChanged = 0
			self.sse = 0
			self.memberOf = [self.masukanVectorKeClusterBerdasarCentroid(i)
								for i in range(len(self.data[1]))]
			print("Jumlah data ke 1", len(self.data[1]))
			print("member of di masukkan ke cluster", self.memberOf)

		def EucledianDistance(self, i, j):
			sumSquares = 0
			for k in range(1, self.kolom):
				sumSquares += (self.data[k][i] - self.centroids[j][k-1])**2
			return math.sqrt(sumSquares)

		def kClustering(self):
			selesai = False
			#self.make_populasi()

			while not selesai:
				self.iterationNumber += 1
				#self.centroids = self.populasi[0]
				#self.updateCentroids()
				self.masukanVectorKeCluster()
				print("jumlah data berubah", self.pointsChanged)

				if float(self.pointsChanged)/len(self.memberOf) < 0.01:
					selesai = True

			print("Jumlah Iterasi: ", self.iterationNumber)
		def pengelompokanData(self):
			akurasi = []
			for centroid in range(len(self.centroids)):
				print("\n\nKelas %i\n---------------" % centroid)
				
				nSetosa = nVirginica = nVersi = 0
				for nama in [self.data[0][i] for i in range(len(self.data[0]))
						if self.memberOf[i] == centroid]:
							#print(nama)
							if nama == "setosa\n":
								nSetosa += 1
							elif nama == "versicolor\n":
								nVersi += 1
							elif nama == "virginica\n":
								nVirginica += 1
				print("Jumlah setosa: ", nSetosa)
				print("Jumlah versi: ", nVersi)
				print("Jumlah virgi: ", nVirginica)
				jumlahMemberCluster = nSetosa+nVirginica+nVersi
				print("Jumlah member cluster: ", jumlahMemberCluster)
				maximum = max(nVersi, nVirginica, nSetosa)
				print("maximum value: ", maximum)
				akurasiCluster = akurasi.append(float(maximum)/float(jumlahMemberCluster))
			#print(akurasi)
			hasilAKurasi = 0
			for i in range(0, len(akurasi)):
				hasilAKurasi += akurasi[i]
			self.akurasi = (hasilAKurasi/3.0)*100
			#print("Accuration: %.2f" % self.akurasi)
			#print("SSE: %.5f" % self.sse)
			return self.centroids, self.sse, self.akurasi
		def coba_saja(self):
			print("centroid coba: ", self.data[1][2])
			print("len self data: ", len(self.data))
			for y in self.data:
				print(y)
			return self.centroids, self.sse

km = KMeans('iris.csv', 3)
km.kClustering()
km.pengelompokanData()








