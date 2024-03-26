package com.campuslands.ADN.services;

import java.util.List;

import com.campuslands.ADN.repositories.entities.Persona;

public interface PersonaService {
    
    List<Persona> findAll();

    Persona findById(Long id);

    Persona save(Persona persona);

    Persona update(Long id, Persona persona);

    void delete(Long id);

    String sospechoso(String cromosoma);
}