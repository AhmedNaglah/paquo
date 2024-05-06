from paquo.projects import QuPathProject


qp = QuPathProject(r'C:\Users\inagl\Downloads\009782_PAS_1of2\009782_PAS_1of2\project')

image = qp.images[0] 
image.hierarchy.annotations  # annotations are stored in a set like proxy object

for annotation in image.hierarchy.annotations:
    print(annotation.name, annotation.path_class, annotation.roi)

print("")