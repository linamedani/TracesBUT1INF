import ardoise.Ardoise;
import ardoise.Forme;
import ardoise.PointPlan;
import ardoise.Segment;

import java.util.ArrayList;

public class applicationArdoise {
    public static void main(String[] args) {
        // Initialisation d'une ardoise vide
        Ardoise ardoise = new Ardoise();

    try {
        // Création + ajout des formes
		ajouterForme(ardoise, new Chapeau("C", new PointPlan(118, 13), new PointPlan(123, 20), new PointPlan(128, 13)));
        ajouterForme(ardoise, new Chapeau("C", new PointPlan(133, 30), new PointPlan(136, 32), new PointPlan(138, 30)));
        ajouterForme(ardoise, new Chapeau("C", new PointPlan(142, 14), new PointPlan(144, 17), new PointPlan(146, 14)));
        ajouterForme(ardoise, new Quadrilatere("Q", new PointPlan(9, 100), new PointPlan(20, 100), new PointPlan(20, 198), new PointPlan(9, 198)));
        ajouterForme(ardoise, new Triangle("T", new PointPlan(170, 52), new PointPlan(173, 45), new PointPlan(177, 52)));
        ajouterForme(ardoise, new Triangle("T", new PointPlan(177, 52), new PointPlan(184, 57), new PointPlan(177, 60)));
        ajouterForme(ardoise, new Triangle("T", new PointPlan(177, 60), new PointPlan(174, 66), new PointPlan(170, 60)));
        ajouterForme(ardoise, new Triangle("T", new PointPlan(170, 60), new PointPlan(164, 57), new PointPlan(170, 52)));
        ajouterForme(ardoise, new Triangle("T", new PointPlan(3, 14), new PointPlan(43, 3), new PointPlan(112, 14)));
        ajouterForme(ardoise, new Triangle("T", new PointPlan(152, 7), new PointPlan(166, 3), new PointPlan(172, 7)));
		
		MultiForme maisonMulti = new MultiForme("GF", 
        new Quadrilatere("Q", new PointPlan(80, 140), new PointPlan(180, 140), new PointPlan(180, 198), new PointPlan(80, 198)),
		new Triangle("T", new PointPlan(80, 140), new PointPlan(130, 100), new PointPlan(180, 140)),
        new Quadrilatere("Q", new PointPlan(120, 170), new PointPlan(140, 170), new PointPlan(140, 198), new PointPlan(120, 198))
		);
		
		ajouterForme(ardoise, maisonMulti);
    } catch (Exception e) {
        System.out.println("Une exception s'est produite : " + e.getMessage());
    }
        // Affichage de l'ardoise
        ardoise.dessinerGraphique();
		
		while (true){
			// Attendre une seconde (900 millisecondes)
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			// Déplacer tous les oiseaux de 10 points en abscisse et 20 points en ordonnée
			ardoise.deplacer("C",10, 20);
		}
		
		
    }




	//Fonction d'ajout
    public static void ajouterForme(Ardoise ardoise, Forme forme) throws Exception {
        String nomForme = forme.typeForme();

        // Récupération des segments de la forme
        ArrayList<Segment> segments = forme.dessiner();

        // Vérification de la valeur de nomForme
        if (!nomForme.equals("Q") && !nomForme.equals("T") && !nomForme.equals("GF") && !nomForme.equals("C")) {
            throw new Exception("Règle violée : La valeur de nomForme doit être Q, T, GF ou C.");
        }

        // Vérification des coordonnées des segments
        for (Segment segment : segments) {
            PointPlan pointDepart = segment.getPointDepart();
            PointPlan pointArrivee = segment.getPointArrivee();

            // Vérification des coordonnées des points par rapport aux limites de l'ardoise
            if (pointDepart.getAbscisse() < 0 || pointDepart.getAbscisse() > 200 || pointDepart.getOrdonnee() < 0 || pointDepart.getOrdonnee() > 200 ||
                    pointArrivee.getAbscisse() < 0 || pointArrivee.getAbscisse() > 200 || pointArrivee.getOrdonnee() < 0 || pointArrivee.getOrdonnee() > 200) {
                throw new Exception("Règle violée : Les coordonnées des points doivent être dans le cadre limité de l'ardoise (200x et 200y points).");
            }
        }

        // Ajout de la forme à l'ardoise
        ardoise.ajouterForme(forme);
    }
}
