package dni;

public class DniCif {
	
		private String dni  = null;
		private Boolean numeroSano = false;
		private Boolean letraSana 	= false;
		// Composici贸n (agregaci贸n) "Has - a" / "Tiene - un"
		private TablaAsignacion tabla = new TablaAsignacion();

		/* Constructores */
		
		public DniCif(String dni) {
			this.dni = dni;
		}
		
		/* Encapsulacion */
		
		public void setDni(String cadena){
			this.dni = cadena;
		}

		public String getDni(){
			return this.dni;
		}
	
		private void setNumeroSano(Boolean valor){
			this.numeroSano = valor;
		}
		
		public Boolean getNumeroSano(){
			return this.numeroSano;
		}
		
		private void setLetraSana(Boolean valor){
			this.letraSana = valor;
		}
	
		public Boolean getLetraSana(){
			return this.letraSana;
		}
		
		/*
		 * L贸gica 
		 */
	
		/* Interfaz P煤blica */
		
		public Boolean checkCIF(){
			return checkDni() && checkLetra();
		}
		
		public Boolean checkDni(){
			setNumeroSano( checkLongitud() && stringEsNumero( getParteNumericaDni() ) );
			return getNumeroSano();
		}
		
		public Boolean checkLetra(){
			if (getNumeroSano() ) {
				setLetraSana ( Character.isUpperCase(getParteAlfabeticaDni()) && checkLetraValida() );
				return getLetraSana();
			}
			else {
				return false;
			}
		}
						
		public Character obtenerLetra(){
			// calcularLetra no puede ejecutarse si antes no se cumplen las condiciones previas en checkDni
			// y checkletra
			if ( getNumeroSano() ){
				return this.tabla.calcularLetra( getParteNumericaDni() );
			}
			else // EXCEPCION: aun no sabemos implementarlas - este c贸digo no es admisible
				return getParteAlfabeticaDni();
		}
	
	
		public Boolean checkLongitud() {
			return getDni().length() == 9;
		}
		// HE MODIFICADO ESTA PARTE DE TU C覦IGO
		public Boolean stringEsNumero(String cadena){
			return this.getDni().matches("\\{8}.");
		}		
			
		public String getParteNumericaDni() {
			return (String) dni.substring(0, dni.length() - 1);
		}
		
		public Character getParteAlfabeticaDni() {
			return dni.charAt(dni.length() - 1);
		}
		
		public Boolean checkLetraValida() {
			if ( getNumeroSano() ) {
				return getParteAlfabeticaDni() == obtenerLetra();
			}
			else
				return false;
		}

}
