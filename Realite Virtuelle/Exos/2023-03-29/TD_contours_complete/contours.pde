//**********************************************************************
// Calcul du gradient de Sobel
// img : PImage image à traiter
// gradient : PImage image du résultat du gradient
//**********************************************************************
void compute_gradient_sobel(PImage img, PImage gradient) {
  float[][] filtreSobelH = { { -1, 0, 1 }, 
    { -2, 0, 2 }, 
    { -1, 0, 1 } }; 
  float[][] filtreSobelV = { { 1, 2, 1 }, 
    { 0, 0, 0 }, 
    { -1, -2, -1 } }; 
  float grad = 0;
  float gradH = 0;
  float gradV = 0;
  int loc = 0;

  //Parcours des pixels de l'image
  for (int x = 1; x < img.width-1; x++) {
    for (int y = 1; y < img.height-1; y++ ) {
      gradV = 0; gradH = 0;      
      //Calcul du résultat de la convolution par les 2 masques :
      gradH = apply_kernel_lum(x, y, filtreSobelH, img);
      gradV = apply_kernel_lum(x, y, filtreSobelV, img);
      //Calcul de la norme du gradient :
      grad = sqrt(gradH*gradH+gradV*gradV); 
      
      //Stockage dans une PImage (valeur entre 0 et 255)
      loc = x + y*img.width;
      gradient.pixels[loc] = color(grad);
    }
  }
  gradient.updatePixels();
}
//**********************************************************************
// Calcul du gradient + nms
// img : PImage image à traiter
// gradient : PImage image du résultat du gradient
// gradnms : PImage image du résultat de la suppression de nom maxima
//**********************************************************************
void compute_gradient_nms(PImage img, PImage gradient, PImage gradnms) {
   // A COMPLETER !
  float[][] filtreSobelH = { { -1, 0, 1 }, 
    { -2, 0, 2 }, 
    { -1, 0, 1 } }; 
  float[][] filtreSobelV = { { 1, 2, 1 }, 
    { 0, 0, 0 }, 
    { -1, -2, -1 } }; 
  float grad = 0;
  float angle = 0;
  float[] gradmag = new float[img.width*img.height];
  float[] gradangle = new float[img.width*img.height];
  float maxgrad = 0; 
  int loc = 0;
  
  //Parcours des pixels de l'image
  for (int x = 1; x < img.width-1; x++) {
    for (int y = 1; y < img.height-1; y++ ) {
      float gradV = 0, gradH=0; 
      //Calcul du résultat de la convolution par les 2 masques :
      gradH = apply_kernel_lum(x, y, filtreSobelH, img);
      gradV = apply_kernel_lum(x, y, filtreSobelV, img);
      //Calcul de la norme du gradient :
      grad = sqrt(gradH*gradH+gradV*gradV);
      if (grad>maxgrad) {
        maxgrad = grad;
      }
      angle = atan2(gradV,gradH);    
      loc = x + y*img.width;      
      gradmag[loc] = grad;
      gradangle[loc] = angle;     
    }
  }
  //NMS
  //Parcours des pixels de l'image
  float pix1 = 0;
  float pix2 = 0;
  float curr_angle = 0;
  for (int x = 1; x < img.width-1; x++) {
    for (int y = 1; y < img.height-1; y++ ) {
      loc = x + y*img.width;
      curr_angle = gradangle[loc]; 
      grad = gradmag[loc];
      // Seuil bas
      if (grad>20){
        gradient.pixels[loc]=color(int(255*grad/maxgrad));
       
        //Gradient vertical
        if ((-0.393<=curr_angle & curr_angle<0.393)||(-3.1416<=curr_angle&curr_angle<-2.749)||(2.749<=curr_angle&curr_angle<=3.1416)){
          pix1 = gradmag[x+(y+1)*img.width];
          pix2 = gradmag[x+(y-1)*img.width];
        }
        //Gradient horizontal
        else if((1.178<=curr_angle & curr_angle<1.964)||(-1.964<=curr_angle&curr_angle<-1.178)){
          pix1 = gradmag[x-1+y*img.width];
          pix2 = gradmag[x+1+y*img.width];
        }
        //Gradient diagonal
        else if((0.393<=curr_angle & curr_angle<1.178)||(-2.749<=curr_angle&curr_angle<-1.964)){
          pix1 = gradmag[x-1+(y+1)*img.width];
          pix2 = gradmag[x+1+(y-1)*img.width]; 
        }
        //Gradient diagonal
        else {
          pix1 = gradmag[x-1+(y-1)*img.width];
          pix2 = gradmag[x+1+(y+1)*img.width];
        }    
        // suppression des non max
        if ((grad>=pix1)&(grad>=pix2)){
          gradnms.pixels[loc]=color(int(255*grad/maxgrad));        
        }else {
          gradnms.pixels[loc]=color(0);}   
      }else{
        gradient.pixels[loc]=color(0);
        gradnms.pixels[loc]=color(0);
      }
      
    }
  }
  gradient.updatePixels(); 
  gradnms.updatePixels();  
    
}


//**********************************************************************
// Seuillage simple
// img : PImage image à traiter
// imgSeuilleeimgSeuillee : PImage image du résultat du seuillage
// seuil : seuil utilisé pour le seuillage simple
//**********************************************************************
void seuillage(PImage img, PImage imgSeuillee, int seuil) {
  int loc = 0;
  for (int x = 0; x < img.width; x++) {
    for (int y = 0; y < img.height; y++ ) {
      // Pixel courant
      loc = x + y*img.width;
      color pix = img.pixels[loc];
      if (brightness(pix) > seuil) {
        imgSeuillee.pixels[loc] = color(255);
      } else {
        imgSeuillee.pixels[loc] = color(0);
      } 
    }
  }
  imgSeuillee.updatePixels();
}


//**********************************************************************
// Calcul des contours : séquence d'opérateurs
// img : PImage image à traiter
// img_lissee : PImage image du résultat du lissage (moyenneur ici)
// gradient : PImage image du résultat du gradient
// gradnms : PImage image du résultat de la suppression de nom maxima
// seuil : seuil utilisé pour le seuillage simple
// contours : PImage image du résultat de l'extraction de contours après seuillage
//**********************************************************************
void compute_contours(PImage img, PImage img_lissee, PImage gradient, PImage gradnms, PImage contours, int seuil) {
  float[][]  masque_lissage = { { 1./9., 1./9., 1./9. }, 
    { 1./9., 1./9., 1./9. }, 
    { 1./9., 1./9., 1/9. } };   
  image_convolution(img, masque_lissage, img_lissee);
  //compute_gradient_sobel(img_lissee, gradient);
  compute_gradient_nms(img_lissee, gradient, gradnms);
  seuillage(gradnms, contours, seuil); 
}
