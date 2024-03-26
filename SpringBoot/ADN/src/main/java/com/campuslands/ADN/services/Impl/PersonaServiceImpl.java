package com.campuslands.ADN.services.Impl;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.campuslands.ADN.repositories.RepositoryPersona;
import com.campuslands.ADN.repositories.entities.Persona;
import com.campuslands.ADN.services.PersonaService;

@Service
public class PersonaServiceImpl implements PersonaService{

    @Autowired
    private RepositoryPersona repositoryPersona;

    @Override
    @Transactional(readOnly = true)
    public List<Persona> findAll() {
        return (List<Persona>) repositoryPersona.findAll();
    }

    @Override
    @Transactional(readOnly = true)
    public Persona findById(Long id) {
        return repositoryPersona.findById(id).orElse(null);
    }

    @Override
    @Transactional
    public Persona save(Persona persona) {
        return repositoryPersona.save(persona);
    }

    @Override
    @Transactional
    public Persona update(Long id, Persona persona) {
        Optional<Persona> personaCurrentOptional = repositoryPersona.findById(id);

        if(personaCurrentOptional.isPresent()){
            Persona personaCurrent = personaCurrentOptional.get();
            personaCurrent.setNombre(persona.getNombre());
            personaCurrent.setApellido(persona.getApellido());
            personaCurrent.setDireccion(persona.getDireccion());
            personaCurrent.setEmail(persona.getEmail());
            personaCurrent.setCromosoma(persona.getCromosoma());

            return personaCurrent;
        }
        return null;
    }

    @Override
    @Transactional
    public void delete(Long id) {
        Optional<Persona> personaOptional = repositoryPersona.findById(id);
        if(personaOptional.isPresent()){
            repositoryPersona.delete(personaOptional.get());
        }
    }

    @Override
    public String sospechoso(String cromosoma) {
        List<Persona> personas = findAll();

        double numMaxCoincidencias = 0;
        Persona persona = null;

        for (Persona p : personas) {
            String cromosomaPersona = p.getCromosoma();
            double numCoincidencias = 0;

            for(int i = 0; i < 20; i++){
                if(cromosoma.charAt(i) == cromosomaPersona.charAt(i)){
                    numCoincidencias++;
                }
            }

            if(numCoincidencias > numMaxCoincidencias){
                numMaxCoincidencias = numCoincidencias;
                persona = p;
            }
        }

        double porcentaje = (numMaxCoincidencias / 20) * 100;

        String mensaje = "La persona con mas coincidencias es: " + persona.getNombre() + " " + persona.getApellido() + "\nCon un porcentaje de coincidencia en su DNA de: %" + porcentaje;

        return mensaje;
    }
    
}
